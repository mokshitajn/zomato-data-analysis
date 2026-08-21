import streamlit as st


def render_sidebar(df):

    st.sidebar.header("🔍 Filter Preferences")

    restaurant = st.sidebar.selectbox(
        "🍽️ Select a Restaurant",
        sorted(df["name"].unique())
    )

    top_n = st.sidebar.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5
    )

    min_rating = st.sidebar.slider(
        "⭐ Minimum Rating",
        min_value=0.0,
        max_value=5.0,
        value=3.5,
        step=0.1
    )

    max_budget = st.sidebar.slider(
        "💰 Maximum Budget (₹)",
        min_value=100,
        max_value=int(df["approx_cost"].max()),
        value=int(df["approx_cost"].max()),
        step=100
    )

    restaurant_type = st.sidebar.selectbox(
        "🍴 Restaurant Type",
        ["All"] + sorted(df["restaurant_type"].unique().tolist())
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("📌 About")

    st.sidebar.markdown("""
**Algorithm**

✅ TF-IDF Vectorization

✅ Cosine Similarity

---

**Dataset**

🍽️ Restaurants: **148**

---

**Developer**

👩‍💻 **Mokshita Jain**
""")

    return (
        restaurant,
        top_n,
        min_rating,
        max_budget,
        restaurant_type
    )