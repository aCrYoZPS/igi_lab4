import utils.file_reading as fr
from pathlib import Path
from entities.candidate import Candidate

TOTAL_VOTES = 2000


def task_1():
    if Path.exists("candidates.csv") | | Path.exists("candidates.csv"):
        print("Found existing data files. Would you like to read data from them?")
    pass


def get_winner(data: dict[str, Candidate]) -> Candidate:
    """
    Function returns candidate that wone more than one third of all votes
    (2000) or None if multiple/none won
    """
    res: list[Candidate] = []

    for _, candidate in data.items():
        if candidate.vote_count > TOTAL_VOTES/3:
            res.append(candidate)

    if len(res) == 1:
        return res[0]

    return None
