from os.path import exists

import pandas as pd


def fix_path(path):
    if exists(path):
        return path
    elif str(path).startswith("../"):
        path = "~/" + str(path)[3:]
        if exists(path):
            return path
    else:
        raise FileNotFound(str(path))


def get_user_rating_counts():
    file_path = fix_path("../data/movies/user_rating_counts.csv")
    return pd.read_csv(file_path, index_col="userId")
