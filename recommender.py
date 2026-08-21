import pandas as pd
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =====================================================
# Load Dataset
# =====================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_zomato.csv")

    df["features"] = (
        df["restaurant_type"].astype(str) + " " +
        df["online_order"].astype(str) + " " +
        df["book_table"].astype(str) + " " +
        df["approx_cost"].astype(str) + " " +
        df["rate"].astype(str)
    )

    return df


# =====================================================
# Build Recommendation Model
# =====================================================

@st.cache_resource
def build_model(df):

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(df["features"])

    similarity_matrix = cosine_similarity(tfidf_matrix)

    indices = pd.Series(
        df.index,
        index=df["name"]
    ).drop_duplicates()

    return similarity_matrix, indices


# =====================================================
# Initialize
# =====================================================

df = load_data()

similarity_matrix, indices = build_model(df)


# =====================================================
# Helper Function
# =====================================================

def get_recommendation_reason(selected, recommended):

    reasons = []

    if selected["restaurant_type"] == recommended["restaurant_type"]:
        reasons.append("🍴 Similar Restaurant Type")

    if abs(selected["approx_cost"] - recommended["approx_cost"]) <= 200:
        reasons.append("💰 Similar Budget")

    if abs(selected["rate"] - recommended["rate"]) <= 0.5:
        reasons.append("⭐ Similar Rating")

    if selected["online_order"] == recommended["online_order"]:
        reasons.append("🛵 Online Ordering Match")

    if selected["book_table"] == recommended["book_table"]:
        reasons.append("📅 Same Table Booking Option")

    return reasons


# =====================================================
# Recommendation Function
# =====================================================

def recommend_restaurants(
    restaurant_name,
    top_n=5,
    min_rating=0,
    max_budget=None,
    restaurant_type="All"
):

    if restaurant_name not in indices:
        return pd.DataFrame()

    selected_idx = indices[restaurant_name]

    selected_restaurant = df.iloc[selected_idx]

    similarity_scores = list(
        enumerate(similarity_matrix[selected_idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for idx, similarity in similarity_scores[1:]:

        row = df.iloc[idx]

        if row["rate"] < min_rating:
            continue

        if max_budget is not None:

            if row["approx_cost"] > max_budget:
                continue

        if restaurant_type != "All":

            if row["restaurant_type"] != restaurant_type:
                continue

        reasons = get_recommendation_reason(
            selected_restaurant,
            row
        )

        recommendations.append({

            "Restaurant": row["name"],

            "Type": row["restaurant_type"],

            "Rating": row["rate"],

            "Cost for Two": row["approx_cost"],

            "Votes": row["votes"],

            "Match Score": round(similarity * 100),

            "Why Recommended": reasons

        })

        if len(recommendations) == top_n:
            break

    return pd.DataFrame(recommendations)


# =====================================================
# Popular Restaurants
# =====================================================

def get_popular_restaurants(n=6):

    popular = df.sort_values(

        by=["rate", "votes"],

        ascending=False

    )

    popular = popular.head(n).copy()

    popular.rename(columns={

        "name": "Restaurant",

        "restaurant_type": "Type",

        "rate": "Rating",

        "approx_cost": "Cost for Two",

        "votes": "Votes"

    }, inplace=True)

    popular["Match Score"] = "🔥"

    popular["Why Recommended"] = [
        ["🔥 Popular Right Now"] for _ in range(len(popular))
    ]

    return popular