import streamlit as st


def render_card_grid(recommendations):
    """
    Display restaurant recommendations in beautiful cards.
    """

    if recommendations.empty:
        st.markdown(
            """
            <div style="
                background:#FFF3CD;
                padding:18px;
                border-radius:15px;
                border-left:8px solid #F5B700;
                font-size:18px;
                font-weight:600;
                color:#6C4E00;
            ">
            ⚠️ No restaurants matched your selected filters.
            Try increasing your budget or lowering the minimum rating.
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown("## 🍽️ Recommended Restaurants")

    cols = st.columns(2)

    for index, (_, row) in enumerate(recommendations.iterrows()):

        with cols[index % 2]:

            st.markdown(
                f"""
<div class="restaurant-card">

<div class="rating-badge">
⭐ {row['Rating']}
</div>

<div class="restaurant-name">
{row['Restaurant']}
</div>

<br>

<span class="restaurant-type">
🍴 {row['Type']}
</span>

<br><br>

<b>💰 Cost for Two:</b> ₹{row['Cost for Two']}<br>

<b>👍 Votes:</b> {row['Votes']}<br>

""",
                unsafe_allow_html=True,
            )

            # Match Score (only if available)
            if "Match Score" in recommendations.columns:

                st.markdown(
                    f"""
<div class="match-score">
🎯 Match Score: {row['Match Score']}%
</div>
""",
                    unsafe_allow_html=True,
                )

            st.markdown(
                """
<br>

<b>Why Recommended?</b>

<div class="reason">🍴 Similar Restaurant Type</div>

<div class="reason">⭐ Similar Rating</div>

<div class="reason">💰 Similar Budget</div>

<div class="reason">🛵 Online Order Match</div>

</div>
""",
                unsafe_allow_html=True,
            )