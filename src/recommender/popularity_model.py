import pandas as pd
from src.recommender import config

# finds the most popular and highly-rated books using a weighted rating system, then returns the top books with their author and cover image information.

def build_popularity_table(books: pd.DataFrame, ratings: pd.DataFrame) -> pd.DataFrame:
    merged = ratings.merge(books, on="ISBN")

    stats = merged.groupby("Book-Title").agg(
        num_ratings=("Book-Rating", "count"),
        avg_rating=("Book-Rating", "mean"),
    ).reset_index()

    # simple weighted score so a book with 2 ratings of 10 doesn't beat one with 500 ratings of 8.5
    C = stats["avg_rating"].mean()
    m = stats["num_ratings"].quantile(0.90)
    
    def weighted_score(row):
        v, R = row["num_ratings"], row["avg_rating"]
        return (v / (v + m)) * R + (m / (v + m)) * C

    stats["weighted_score"] = stats.apply(weighted_score, axis=1)
    stats = stats.merge(books[["Book-Title", "Book-Author", "Image-URL-M"]].drop_duplicates("Book-Title"), on="Book-Title", how="left")

    top_books = stats.sort_values("weighted_score", ascending=False).head(config.TOP_N_POPULAR)
    return top_books.reset_index(drop=True)