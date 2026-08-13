import pickle
from src.recommender import config
from src.recommender.data_loader import load_all
from src.recommender.preprocessing import build_pivot_table
from src.recommender.popularity_model import build_popularity_table
from src.recommender.collaborative_model import compute_similarity

def save_pickle(obj, filename):
    with open(config.MODELS_DIR / filename, "wb") as f:
        pickle.dump(obj, f)

def main():
    print("Loading data...")
    books, users, ratings = load_all()

    print("Building popularity table...")
    popular_df = build_popularity_table(books, ratings)
    save_pickle(popular_df, "popular_books.pkl")

    print("Building pivot table...")
    pivot = build_pivot_table(books, ratings)
    save_pickle(pivot, "pivot_table.pkl")

    print("Computing similarity matrix...")
    similarity = compute_similarity(pivot)
    save_pickle(similarity, "similarity_scores.pkl")

    save_pickle(books, "books_meta.pkl")

    print(f"Done. Pivot table shape: {pivot.shape}")
    print(f"Popular books: {len(popular_df)} | Similarity matrix: {similarity.shape}")

if __name__ == "__main__":
    main()