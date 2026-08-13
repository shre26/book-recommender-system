from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
MODELS_DIR = BASE_DIR / "models"

BOOKS_CSV = RAW_DATA_DIR / "Books.csv"
USERS_CSV = RAW_DATA_DIR / "Users.csv"
RATINGS_CSV = RAW_DATA_DIR / "Ratings.csv"

# experienced readers min book review count of 200 & book used for model training for reccomendation must have minimum 50 ratings
MIN_RATINGS_PER_USER = 200
MIN_RATINGS_PER_BOOK = 50

TOP_N_POPULAR = 50
TOP_N_RECOMMEND = 5

MODELS_DIR.mkdir(parents=True, exist_ok=True)