import streamlit as st


def render_metrics(df):
    """
    Display dashboard metrics.
    """

    total_restaurants = len(df)
    avg_rating = round(df["rate"].mean(), 2)
    avg_cost = int(df["approx_cost"].mean())

    online_percentage = round(
        (df["online_order"] == "Yes").sum()
        / len(df)
        * 100,
        1,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🍽️ Restaurants</div>
            <div class="metric-value">{total_restaurants}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⭐ Average Rating</div>
            <div class="metric-value">{avg_rating}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Average Cost</div>
            <div class="metric-value">₹{avg_cost}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🛵 Online Orders</div>
            <div class="metric-value">{online_percentage}%</div>
        </div>
        """, unsafe_allow_html=True)