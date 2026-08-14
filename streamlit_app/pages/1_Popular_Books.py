import sys
import streamlit as st
from html import escape
from pathlib import Path
from streamlit_app.utils import load_popular_books

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

def html_block(s):
    return "\n".join(line.strip() for line in s.strip().splitlines())

def render_html(s):
    st.markdown(html_block(s), unsafe_allow_html=True)

def load_css():
    css_path = PROJECT_ROOT / "streamlit_app" / "style.css"
    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Popular Books", page_icon="🏆", layout="wide")

load_css()

render_html(
    """
    <div class="page-header">
        <div class="page-header-icon">🏆</div>
        <div>
            <h1>Most Popular Books</h1>
            <p>Discover books ranked using rating count and average rating.</p>
        </div>
    </div>
    """)

popular_df = load_popular_books()

cols_per_row = 4

for start in range(0, len(popular_df), cols_per_row):

    row = popular_df.iloc[start:start + cols_per_row]
    cols = st.columns(cols_per_row, gap="large")
    for col, (_, book) in zip(cols, row.iterrows()):
        with col:
            image_url = book["Image-URL-M"]
            if not isinstance(image_url, str) or not image_url.strip():
                image_url = "https://placehold.co/200x280?text=No+Cover"
            image_url = escape(str(image_url), quote=True)

            title = escape(str(book["Book-Title"]))
            author = escape(str(book["Book-Author"]))

            avg_rating = float(book["avg_rating"])
            num_ratings = int(book["num_ratings"])

            render_html(
                f"""
                <div class="book-card">
                    <div class="book-cover-wrap">
                        <img src="{image_url}" class="book-cover"/>
                    </div>
                    <div class="book-info">
                        <div class="book-title" title="{title}">{title}</div>
                        <div class="book-author" title="{author}"> by {author} </div>
                        <div class="book-rating">
                            ⭐ {avg_rating:.1f}
                            <span class="rating-count">({num_ratings:,} ratings)</span>
                        </div>
                    </div>
                </div>
                """)

render_html(
    """
    <div class="footer">Showing books ranked by popularity and weighted rating.</div>
    """)