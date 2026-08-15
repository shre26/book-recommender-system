import pytest
import pickle
from src.recommender import config
from src.recommender.collaborative_model import recommend


@pytest.fixture(scope="module")
def pivot_and_similarity():
    with open(config.MODELS_DIR / "pivot_table.pkl", "rb") as f:
        pivot = pickle.load(f)
    with open(config.MODELS_DIR / "similarity_scores.pkl", "rb") as f:
        similarity = pickle.load(f)
    return pivot, similarity


def test_recommend_returns_k_results(pivot_and_similarity):
    pivot, similarity = pivot_and_similarity
    results = recommend(pivot.index[0], pivot, similarity, k=5)
    assert len(results) == 5

def test_recommend_excludes_the_book_itself(pivot_and_similarity):
    pivot, similarity = pivot_and_similarity
    book = pivot.index[0]
    results = recommend(book, pivot, similarity, k=5)
    titles = [title for title, _ in results]
    assert book not in titles

def test_recommend_unknown_book_returns_empty(pivot_and_similarity):
    pivot, similarity = pivot_and_similarity
    results = recommend("This Book Does Not Exist 12345", pivot, similarity)
    assert results == []

def test_similarity_scores_are_valid_range(pivot_and_similarity):
    pivot, similarity = pivot_and_similarity
    results = recommend(pivot.index[0], pivot, similarity, k=5)
    assert all(-1.0 <= score <= 1.0 for _, score in results)