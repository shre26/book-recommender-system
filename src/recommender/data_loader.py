import pandas as pd
from src.recommender import config

def load_books() -> pd.DataFrame:
    books = pd.read_csv(config.BOOKS_CSV, sep=",", encoding="latin-1", low_memory=False)
    books = books[["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-M"]]
    return books

def load_users() -> pd.DataFrame:
    return pd.read_csv(config.USERS_CSV, sep=",", encoding="latin-1", low_memory=False)

def load_ratings() -> pd.DataFrame:
    return pd.read_csv(config.RATINGS_CSV, sep=",", encoding="latin-1", low_memory=False)

def load_all():
    return load_books(), load_users(), load_ratings()