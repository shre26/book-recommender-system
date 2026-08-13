import pickle
from src.recommender.collaborative_model import recommend

with open("models/pivot_table.pkl", "rb") as f:
    pivot = pickle.load(f)
with open("models/similarity_scores.pkl", "rb") as f:
    sim = pickle.load(f)

print(pivot.index[:20])  # eyeball some book titles that exist
print(recommend(pivot.index[0], pivot, sim))