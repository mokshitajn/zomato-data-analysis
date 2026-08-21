import streamlit as st
from recommender import recommend_restaurants, df

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Zomato Restaurant Recommender",
    page_icon="🍽️",
    layout="wide"
)

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------
# Direction: maroon + cream + yellow (the version that landed best), with a
# new prominent search box added right under the hero. Streamlit's
# selectbox is technically searchable already, but a dedicated search input
# at the top of the page reads as "app-like" the way Zomato/Blinkit's own
# search bars do, rather than something buried in a form control.

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700;900&family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --cream: #FBF1DC;
        --card: #FFFDF6;
        --card-hover: #FFF6DE;
        --maroon: #7A2530;
        --maroon-deep: #5E1C25;
        --yellow: #FFC300;
        --yellow-deep: #E6AC00;
        --ink: #2B1B12;
        --muted: #8A7A63;
        --hairline: #E8D8B8;
        --green-bg: #E4F8F0;
        --green: #0CA678;
    }

    .stApp {
        background-color: var(--cream);
        color: var(--ink);
    }

    /* Sidebar -- filled maroon panel */
    section[data-testid="stSidebar"] {
        background-color: var(--maroon);
        border-right: 6px solid var(--yellow);
    }
    section[data-testid="stSidebar"] * {
        color: #FBEFD8 !important;
    }
    section[data-testid="stSidebar"] h2 {
        font-family: 'Fraunces', serif !important;
        font-weight: 700;
        color: #FFFFFF !important;
        font-size: 1.4rem;
        border-bottom: 3px solid var(--yellow);
        padding-bottom: 0.6rem;
        margin-bottom: 1rem;
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] input {
        background-color: var(--maroon-deep) !important;
        border: 1.5px solid var(--yellow) !important;
        border-radius: 10px !important;
        color: #FBEFD8 !important;
    }
    section[data-testid="stSidebar"] [data-baseweb="slider"] div[role="slider"] {
        background-color: var(--yellow) !important;
        border-color: #FFFFFF !important;
    }

    h1, h2, h3 {
        font-family: 'Fraunces', serif !important;
        color: var(--ink);
    }
    body, p, span, div, label {
        font-family: 'Inter', sans-serif;
    }

    /* Hero */
    .hero-eyebrow {
        display: inline-block;
        background-color: var(--yellow);
        color: #4A3200;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 1.1rem;
        box-shadow: 3px 3px 0px 0px var(--maroon);
    }
    .hero-title {
        font-family: 'Fraunces', serif;
        font-weight: 900;
        font-size: 3.4rem;
        color: var(--ink);
        margin: 0;
        line-height: 1.05;
    }
    .hero-title span {
        color: var(--maroon);
    }
    .hero-subtitle {
        color: var(--muted);
        font-size: 1.15rem;
        margin-top: 0.9rem;
        max-width: 660px;
        line-height: 1.6;
    }

    /* Search box */
    .search-wrap {
        margin-top: 1.6rem;
        margin-bottom: 0.4rem;
    }
    .search-wrap .stTextInput > div > div {
        background-color: var(--card) !important;
        border: 3px solid var(--maroon) !important;
        border-radius: 999px !important;
        box-shadow: 5px 5px 0px 0px var(--yellow);
        padding-left: 0.4rem;
    }
    .search-wrap .stTextInput input {
        color: var(--ink) !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        padding: 0.7rem 1rem !important;
    }
    .search-wrap .stTextInput input::placeholder {
        color: var(--muted) !important;
    }
    .search-hint {
        color: var(--muted);
        font-size: 0.85rem;
        margin-top: 0.5rem;
        margin-left: 0.5rem;
    }

    .thick-rule {
        border: none;
        height: 6px;
        background: repeating-linear-gradient(90deg, var(--maroon) 0 20px, var(--yellow) 20px 40px);
        border-radius: 6px;
        margin: 2rem 0;
    }

    .section-title {
        font-family: 'Fraunces', serif;
        font-weight: 700;
        font-size: 1.6rem;
        color: var(--ink);
        margin-bottom: 0.2rem;
    }
    .section-subtitle {
        color: var(--muted);
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: var(--card);
        border: 2px solid var(--hairline);
        border-radius: 16px;
        padding: 1.3rem 1.5rem;
        box-shadow: 5px 5px 0px 0px var(--hairline);
    }
    div[data-testid="stMetricLabel"] {
        color: var(--muted) !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    div[data-testid="stMetricValue"] {
        color: var(--maroon) !important;
        font-family: 'Fraunces', serif !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
    }

    /* Primary button */
    .stButton > button {
        background-color: var(--maroon) !important;
        color: #FBEFD8 !important;
        border: 2px solid var(--maroon) !important;
        border-radius: 999px !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.02em;
        padding: 0.95rem 1.3rem !important;
        box-shadow: 6px 6px 0px 0px var(--yellow);
        transition: transform 0.12s ease, box-shadow 0.12s ease;
    }
    .stButton > button:hover {
        background-color: var(--maroon-deep) !important;
        color: #FFFFFF !important;
        transform: translate(-3px, -3px);
        box-shadow: 9px 9px 0px 0px var(--yellow);
    }
    .stButton > button:active {
        transform: translate(0px, 0px);
        box-shadow: 2px 2px 0px 0px var(--yellow);
    }

    /* Recommendation / popular / search-result card */
    .food-card {
        background-color: var(--card);
        border: 2px solid var(--hairline);
        border-radius: 18px;
        padding: 1.4rem 1.5rem;
        height: 100%;
        transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
        box-shadow: 6px 6px 0px 0px var(--hairline);
    }
    .food-card:hover {
        transform: translate(-3px, -3px);
        border-color: var(--maroon);
        box-shadow: 8px 8px 0px 0px var(--yellow);
        background-color: var(--card-hover);
    }
    .food-card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 0.5rem;
        margin-bottom: 0.6rem;
    }
    .food-card-name {
        font-family: 'Fraunces', serif;
        font-weight: 700;
        font-size: 1.3rem;
        color: var(--ink);
        margin: 0;
        line-height: 1.3;
    }
    .rating-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        background-color: var(--yellow);
        color: #4A3200;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 0.25rem 0.65rem;
        border-radius: 8px;
        white-space: nowrap;
        box-shadow: 2px 2px 0px 0px var(--maroon);
    }
    .star-icon {
        font-family: Arial, "Segoe UI Symbol", "Noto Sans Symbols", sans-serif;
        font-size: 0.95rem;
        line-height: 1;
    }
    .food-pill {
        display: inline-block;
        background-color: var(--green-bg);
        color: var(--green);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.9rem;
    }
    .food-stats {
        display: flex;
        justify-content: space-between;
        border-top: 2px dashed var(--hairline);
        padding-top: 0.75rem;
        margin-top: 0.4rem;
    }
    .food-stat-label {
        font-size: 0.7rem;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.15rem;
    }
    .food-stat-value {
        font-family: 'Fraunces', serif;
        font-weight: 700;
        font-size: 1.2rem;
        color: var(--maroon);
    }

    .menu-footer {
        text-align: center;
        color: var(--muted);
        font-size: 0.9rem;
        margin-top: 2.4rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("""
<span class="hero-eyebrow">TF-IDF &middot; Cosine Similarity &middot; Machine Learning</span>
<p class="hero-title">Find your next <span>favorite table</span> 🍽️</p>
<p class="hero-subtitle">
    Tell us a restaurant you already love, and this content-based recommender
    digs up the closest matches on the menu — by cuisine, price, and vibe.
</p>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Search Box
# --------------------------------------------------

st.markdown('<div class="search-wrap">', unsafe_allow_html=True)
search_query = st.text_input(
    "Search restaurants",
    placeholder="🔍  Search restaurants by name...",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# All names in the dataset, and the subset matching the current search text
all_names = sorted(df["name"].unique())

if search_query.strip():
    matched_names = sorted(
        df[df["name"].str.contains(search_query, case=False, na=False)]["name"].unique()
    )
    st.markdown(
        f'<p class="search-hint">Found {len(matched_names)} match(es) for "{search_query}"</p>',
        unsafe_allow_html=True
    )
else:
    matched_names = all_names

st.markdown('<hr class="thick-rule">', unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("🔍 Filter Preferences")

# The sidebar dropdown narrows to search matches automatically; falls back
# to the full list if the search box is empty or matches nothing.
dropdown_options = matched_names if matched_names else all_names

restaurant = st.sidebar.selectbox(
    "Select a Restaurant",
    dropdown_options
)

top_n = st.sidebar.slider(
    "Number of Recommendations",
    1,
    10,
    5
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    0.0,
    5.0,
    3.5,
    0.1
)

max_budget = st.sidebar.slider(
    "Maximum Budget (₹)",
    100,
    int(df["approx_cost"].max()),
    int(df["approx_cost"].max()),
    100
)

restaurant_type = st.sidebar.selectbox(
    "Restaurant Type",
    ["All"] + sorted(df["restaurant_type"].unique().tolist())
)

# --------------------------------------------------
# Dataset Statistics
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Restaurants Listed", len(df))

with col2:
    st.metric("Average Rating", round(df["rate"].mean(), 2))

with col3:
    st.metric("Average Cost for Two", f"₹{int(df['approx_cost'].mean())}")

st.markdown('<hr class="thick-rule">', unsafe_allow_html=True)


# --------------------------------------------------
# Helper: render a row of food cards from a dataframe slice
# --------------------------------------------------

def render_card_grid(rows_df, name_col="name", type_col="restaurant_type",
                      rating_col="rate", cost_col="approx_cost", votes_col="votes"):

    rows = list(rows_df.iterrows())

    for i in range(0, len(rows), 3):

        cols = st.columns(3)

        for col, (_, row) in zip(cols, rows[i:i + 3]):

            rating_val = float(row[rating_col])

            with col:
                st.markdown(f"""
                <div class="food-card">
                    <div class="food-card-top">
                        <p class="food-card-name">{row[name_col]}</p>
                        <span class="rating-badge"><span class="star-icon">&#9733;</span> {rating_val}</span>
                    </div>
                    <span class="food-pill">{row[type_col]}</span>
                    <div class="food-stats">
                        <div>
                            <div class="food-stat-label">Cost for Two</div>
                            <div class="food-stat-value">₹{int(row[cost_col])}</div>
                        </div>
                        <div>
                            <div class="food-stat-label">Votes</div>
                            <div class="food-stat-value">{int(row[votes_col])}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# --------------------------------------------------
# Recommendation Button
# --------------------------------------------------

clicked = st.button("🍽️  Recommend Restaurants", use_container_width=True)

if clicked:

    recommendations = recommend_restaurants(
        restaurant_name=restaurant,
        top_n=top_n,
        min_rating=min_rating,
        max_budget=max_budget,
        restaurant_type=restaurant_type
    )

    if recommendations.empty:

        st.warning("No restaurants match your selected filters. Try loosening the rating or budget range.")

    else:

        st.success(f"Found {len(recommendations)} restaurant(s) similar to {restaurant}.")

        st.markdown('<p class="section-title">Recommended For You</p>', unsafe_allow_html=True)

        render_card_grid(
            recommendations.rename(columns={
                "Restaurant": "name",
                "Type": "restaurant_type",
                "Rating": "rate",
                "Cost for Two": "approx_cost",
                "Votes": "votes"
            })
        )

elif search_query.strip():

    # --------------------------------------------------
    # Search results view -- shown while the user is typing a query
    # --------------------------------------------------

    search_results = df[df["name"].str.contains(search_query, case=False, na=False)]

    st.markdown('<p class="section-title">Search Results</p>', unsafe_allow_html=True)

    if search_results.empty:
        st.warning(f'No restaurants found matching "{search_query}". Try a different name.')
    else:
        st.markdown(
            f'<p class="section-subtitle">Showing {len(search_results)} restaurant(s) matching your search.</p>',
            unsafe_allow_html=True
        )
        render_card_grid(search_results)

else:

    # --------------------------------------------------
    # Popular Right Now -- default view so the page isn't empty pre-click
    # --------------------------------------------------

    st.markdown('<p class="section-title">🔥 Popular Right Now</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">Top-rated picks across the whole list, in case you\'re not sure where to start.</p>',
        unsafe_allow_html=True
    )

    popular = df.sort_values(by=["rate", "votes"], ascending=False).head(6)

    render_card_grid(popular)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown('<hr class="thick-rule">', unsafe_allow_html=True)
st.markdown('<p class="menu-footer">Built using Python, Scikit-learn and Streamlit</p>', unsafe_allow_html=True)