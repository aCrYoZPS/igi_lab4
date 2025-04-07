import csv
import pickle
from entities.candidate import Candidate


def read_csv() -> dict[str, Candidate]:
    res = {}
    with open("candidates.csv") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=" ")
        for row in reader:
            res[row["surname"]] = Candidate(row["surname"], row["vote_count"])

    return res


def read_pickle() -> dict[str, Candidate]:
    with open("candidates.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)
