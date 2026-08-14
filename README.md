# 📚 Book Recommendation System

A collaborative-filtering based book recommender, built on the [Book-Crossing dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).

🔗 **Live demo:** _coming soon_

## Overview

This project recommends books using two approaches:
- **Popularity-based** — top books ranked by a weighted score of rating count and average rating (good for new/cold-start users)
- **Item-based collaborative filtering** — recommends books similar to a chosen title, based on cosine similarity between books' rating patterns across users

## Dataset

[Book-Crossing Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) — ~270k books, ~1.1M ratings from ~278k users.

## Tech Stack

- **Data processing:** pandas, numpy
- **Modeling:** scikit-learn (cosine similarity)
- **App/UI:** Streamlit
- **Deployment:** Streamlit Community Cloud

## Project Structure
```
book-recommender-system/
├── data/               # raw & processed data (not committed)
├── notebooks/          # EDA and experimentation
├── src/recommender/    # core pipeline: preprocessing, models, training
├── models/             # trained artifacts (pickled)
├── streamlit_app/      # the deployed app
└── tests/              # unit tests
```

## How It Works

1. Filter to active users (200+ ratings) and popular books (50+ ratings) to keep the similarity matrix dense and meaningful
2. Build a Book × User rating pivot table
3. Compute cosine similarity between books based on their rating vectors
4. For a given book, return the top-K most similar books

## Running Locally

```bash
git clone https://github.com/shre26/book-recommender-system.git
cd book-recommender-system

python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# download the dataset from Kaggle, place CSVs in data/raw/

# generate model artifacts
python -m src.recommender.train

# launch the app
streamlit run streamlit_app/app.py
```

## Sample Output

Recommending books similar to **"1984"**:
- Animal Farm
- The Handmaid's Tale
- The Catcher in the Rye
- Lord of the Flies
- Slaughterhouse-Five

## License

MIT