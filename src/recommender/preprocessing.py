import pandas as pd
from src.recommender import config

def merge_books_ratings(books: pd.DataFrame, ratings: pd.DataFrame) -> pd.DataFrame:
    return ratings.merge(books, on="ISBN")

def get_active_users(ratings:pd.DataFrame, min_ratings: int ) -> pd.Index:
    counts = ratings.groupby("User-ID")["Book-Rating"].count()
    return counts[counts >= min_ratings].index

def get_popular_books(ratings_books: pd.DataFrame, min_ratings: int) -> pd.Index:
    counts = ratings_books.groupby("Book-Title")["Book-Rating"].count()
    return counts[counts >= min_ratings].index

# Returns a Book-Title x User-ID matrix of ratings, filtered to active users & popular books
def build_pivot_table(books: pd.DataFrame, ratings: pd.DataFrame) -> pd.DataFrame:
    merged = merge_books_ratings(books, ratings)

    active_users = get_active_users(ratings, config.MIN_RATINGS_PER_USER)
    filtered = merged[merged["User-ID"].isin(active_users)]

    popular_books = get_popular_books(filtered, config.MIN_RATINGS_PER_BOOK)
    filtered = filtered[filtered["Book-Title"].isin(popular_books)]

    pivot = filtered.pivot_table(
        index="Book-Title", columns="User-ID", values="Book-Rating", aggfunc="mean", fill_value=0
    )

    return pivot