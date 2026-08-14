import streamlit as st
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "style.css"
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)

st.set_page_config(page_title="Book Recommender", page_icon="📚", layout="wide")

load_css()

st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">📚</div>
        <h1>Discover Your Next Great Read</h1>
        <p>Find books loved by readers and discover titles similar
            to the books you already enjoy. </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-heading">
        <h2>Explore Books</h2>
        <p>Choose how you want to discover your next book.</p>
    </div>
   """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🏆</div>
            <h3>Popular Books</h3>
            <p> Explore highly-rated books that are loved by
                a large number of readers.</p>
        </div>
        """, unsafe_allow_html=True)


with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <h3>Similar Books</h3>
            <p>Choose a book you enjoyed and discover titles
                with similar reader preferences.</p>
        </div>
        """, unsafe_allow_html=True)


with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>Smart Recommendation</h3>
            <p>Recommendations are generated using item-based
                collaborative filtering.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-heading section-spacing">
        <h2>How It Works</h2>
        <p>Three simple steps to discover your next book.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="how-card">
        <div class="how-step">
            <span>1</span>
            <div>
                <h4>Choose a Book</h4>
                <p>Select a book that you already enjoy.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="how-card">
        <div class="how-step">
            <span>2</span>
            <div>
                <h4>Analyze Reader Patterns</h4>
                <p>The system compares rating patterns across
                    thousands of readers.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="how-card">
        <div class="how-step">
            <span>3</span>
            <div>
                <h4>Get Recommendations</h4>
                <p>Receive books with similar rating patterns
                    using cosine similarity.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="dataset-card">
        <div>
            <h3>📖 About the Dataset</h3>
            <p>This project uses the
                <a href="https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset"
                   target="_blank">
                    Book-Crossing Dataset
                </a>, containing books, users and more than one million ratings.
            </p>
        </div>
        <div class="dataset-badge">Book-Crossing</div>
    </div>
    """, unsafe_allow_html=True)