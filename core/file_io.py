import csv
import pickle
from entities.candidate import Candidate


def read_txt() -> str:
    with open("text.txt", "rb") as file:
        return file.read().decode("utf-8")


def read_csv() -> dict[str, Candidate]:
    res = {}
    with open("candidates.csv") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            res[row["surname"]] = Candidate(row["surname"], row["vote_count"])

    return res


def write_csv(data: dict[str, Candidate]):
    with open("candidates.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(["surname", "vote_count"])
        for surname, candidate in data.items():
            writer.writerow([surname, candidate.vote_count])


def read_pickle() -> dict[str, Candidate]:
    with open("candidates.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)


def write_pickle(data: dict[str, Candidate]):
    with open("candidates.pkl", "wb") as pickle_file:
        pickle.dump(data, pickle_file)
