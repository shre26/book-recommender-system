import pytest
from src.recommender.data_loader import load_books, load_ratings
from src.recommender.popularity_model import build_popularity_table
from src.recommender import config


@pytest.fixture(scope="module")
def popular_df():
    books = load_books()
    ratings = load_ratings()
    return build_popularity_table(books, ratings)


def test_returns_correct_number_of_books(popular_df):
    assert len(popular_df) == config.TOP_N_POPULAR

def test_all_books_meet_min_ratings_threshold(popular_df):
    assert (popular_df["num_ratings"] >= config.MIN_RATINGS_PER_BOOK).all()

def test_sorted_by_weighted_score_descending(popular_df):
    scores = popular_df["weighted_score"].tolist()
    assert scores == sorted(scores, reverse=True)

def test_no_duplicate_titles(popular_df):
    assert popular_df["Book-Title"].is_unique

def test_ratings_within_valid_range(popular_df):
    assert popular_df["avg_rating"].between(0, 10).all()