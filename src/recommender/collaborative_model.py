import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.recommender import config

def compute_similarity(pivot_table) -> np.ndarray:
    return cosine_similarity(pivot_table.values)

def recommend(book_title: str, pivot_table, similarity_scores, k: int = None):
    k = k or config.TOP_N_RECOMMEND
    if book_title not in pivot_table.index:
        return []

    idx = np.where(pivot_table.index == book_title)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[idx])), key=lambda x: x[1], reverse=True
    )[1:k+1]    # skipping idx 0 as its the book itself

    return [(pivot_table.index[i], score) for i, score in similar_items]
