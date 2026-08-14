import pickle
import streamlit as st
from src.recommender import config


@st.cache_resource
def load_pivot_table():
    with open(config.MODELS_DIR / "pivot_table.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_similarity_scores():
    with open(config.MODELS_DIR / "similarity_scores.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_popular_books():
    with open(config.MODELS_DIR / "popular_books.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_books_meta():
    with open(config.MODELS_DIR / "books_meta.pkl", "rb") as f:
        return pickle.load(f)

def get_book_image(books_meta, title, default="https://placehold.co/150x220?text=No+Cover"):
    row = books_meta[books_meta["Book-Title"] == title]
    if row.empty or pandas_isna(row.iloc[0]["Image-URL-M"]):
        return default
    return row.iloc[0]["Image-URL-M"]

def pandas_isna(val):
    import pandas as pd
    return pd.isna(val)