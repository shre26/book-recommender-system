# src/recommender/popularity_model.py
import pandas as pd
from src.recommender import config

def build_popularity_table(books: pd.DataFrame, ratings: pd.DataFrame, min_ratings: int = None) -> pd.DataFrame:
    min_ratings = min_ratings or config.MIN_RATINGS_PER_BOOK

    merged = ratings.merge(books, on="ISBN")

    stats = merged.groupby("Book-Title").agg(
        num_ratings=("Book-Rating", "count"),
        avg_rating=("Book-Rating", "mean"),
    ).reset_index()

    # only consider books with enough ratings to be statistically meaningful
    stats = stats[stats["num_ratings"] >= min_ratings]

    C = stats["avg_rating"].mean()
    m = stats["num_ratings"].quantile(0.90)

    def weighted_score(row):
        v, R = row["num_ratings"], row["avg_rating"]
        return (v / (v + m)) * R + (m / (v + m)) * C

    stats["weighted_score"] = stats.apply(weighted_score, axis=1)
    stats = stats.merge(
        books[["Book-Title", "Book-Author", "Image-URL-M"]].drop_duplicates("Book-Title"),
        on="Book-Title", how="left"
    )

    top_books = stats.sort_values("weighted_score", ascending=False).head(config.TOP_N_POPULAR)
    return top_books.reset_index(drop=True)