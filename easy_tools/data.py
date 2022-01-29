import pandas as pd


def get_user_rating_counts():
    return pd.read_csv("../data/movies/user_rating_counts.csv", index_col="userId")
