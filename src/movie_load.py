from pathlib import Path

import pandas as pd


def movie_data_collect():
    # Build a reliable path from this file so it works from any working directory.
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "TMDB_movie_dataset_v11.csv"

    movies = pd.read_csv(csv_path)
    return movies


