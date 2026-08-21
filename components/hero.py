import streamlit as st


def render_hero():

    st.markdown(
        """
        <div class="hero-badge">
            🍽️ AI POWERED RESTAURANT RECOMMENDER
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
            Find Your Next Favorite Restaurant
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtitle">
            Discover restaurants you'll love using a Machine Learning recommendation engine
            powered by <b>TF-IDF Vectorization</b> and <b>Cosine Similarity</b>.
        </div>
        """,
        unsafe_allow_html=True
    )