import streamlit as st
import sys
from pathlib import Path
from html import escape

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.recommender.collaborative_model import recommend
from streamlit_app.utils import load_pivot_table, load_similarity_scores, load_books_meta

def html_block(s: str) -> str:
    return "\n".join(line.strip() for line in s.strip().splitlines())

def render_html(s: str):
    st.markdown(html_block(s), unsafe_allow_html=True)

def load_css():
    css_path = PROJECT_ROOT / "streamlit_app" / "style.css"

    if not css_path.exists():
        st.warning(f"Stylesheet not found at {css_path}. Continuing without custom styles.")
        return

    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Recommend Books",
    page_icon="📚",
    layout="wide"
)

load_css()

render_html("""
    <div class="page-header">
        <div class="page-header-icon">📚</div>
        <div>
            <h1>Find Your Next Read</h1>
            <p>Choose a book you enjoyed and discover five similar titles.</p>
        </div>
    </div>
""")

try:
    pivot = load_pivot_table()
    similarity = load_similarity_scores()
    books_meta = load_books_meta()
except Exception as e:
    st.error(f"Failed to load model data: {e}")
    st.stop()

render_html("""
    <div class="selection-heading">
        <h3>🔎 Choose a book you enjoyed</h3>
        <p>We'll find books with similar reader rating patterns.</p>
    </div>
""")

book_list = sorted(pivot.index.tolist())

selected_book = st.selectbox("Select a book", book_list, label_visibility="collapsed")

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
with button_col2:
    recommend_clicked = st.button("✨ Find Similar Books", type="primary", use_container_width=True)

results = []

if recommend_clicked:
    with st.spinner("Finding similar books..."):
        results = recommend(selected_book, pivot, similarity, k=5)
    if not results:
        st.warning("No recommendations were found for this book.")
    else:
        selected_book_safe = escape(str(selected_book))
        render_html(f"""
            <div class="recommendation-heading">
                <h2>Because you liked<em>{selected_book_safe}</em></h2>
                <p>Here are five books with similar reader preferences.</p>
            </div>
        """)

        cols = st.columns(5, gap="large")

        for col, (title, score) in zip(cols, results):
            with col:
                meta_row = books_meta[books_meta["Book-Title"] == title]
                if (not meta_row.empty and isinstance(meta_row.iloc[0]["Image-URL-M"], str) and meta_row.iloc[0]["Image-URL-M"].strip()):
                    image_url = meta_row.iloc[0]["Image-URL-M"]
                else:
                    image_url = "https://placehold.co/200x280?text=No+Cover"

                if not meta_row.empty:
                    author = meta_row.iloc[0]["Book-Author"]
                else:
                    author = "Unknown"

                title_safe = escape(str(title))
                author_safe = escape(str(author))
                image_url_safe = escape(str(image_url), quote=True)
                score = float(score)

                card_html = f"""
                    <div class="book-card recommendation-card">
                        <div class="book-cover-wrap">
                            <img src="{image_url_safe}" class="book-cover">
                        </div>
                        <div class="book-info">
                            <div class="book-title" title="{title_safe}">{title_safe}</div>
                            <div class="book-author" title="{author_safe}">by {author_safe}</div>
                            <div class="similarity-badge">✨ {score:.2f} similarity</div>
                        </div>
                    </div>
                """
                render_html(card_html)

if recommend_clicked and results:
    render_html("""
        <div class="explanation-card">
            <h3>💡 How were these books selected?</h3>
            <p>
                The recommender compares the rating patterns of
                readers across books. Cosine similarity is then
                used to identify titles with similar reader
                preferences.
            </p>
        </div>
    """)