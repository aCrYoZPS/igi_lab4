import utils.file_reading as fr
from entities.candidate import Candidate

TOTAL_VOTES = 2000


def task_1():
    pass


def get_winners() -> list[Candidate]:
    """
    Function returns list of candidates that have more than one third of all votes
    (2000)
    """
    file_type = input("Select file type (csv, pkl)")
    candidates: dict[Candidate, int] = {}
    res: list[Candidate] = []
    match file_type:
        case "csv":
            candidates = fr.read_csv()
        case "pkl":
            candidates = fr.read_csv()
        case _:
            raise RuntimeError("Wrong file type")

    for candidate, votes in candidates.items():
        if votes > TOTAL_VOTES/3:
            res.append(candidate)

    return res
