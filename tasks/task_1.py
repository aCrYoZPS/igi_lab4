from core.io import y_n_question, IOCommand, print_collection_table
import core.file_io as file_io
from core.globals import ACTION_YES, ACTION_QUIT, ACTION_NO
from pathlib import Path
from entities.candidate import Candidate

TOTAL_VOTES = 2000


def task_1():
    data: dict[str, Candidate] = {}

    if Path.exists(Path("candidates.csv")) or Path.exists(Path("candidates.csv")):
        command: IOCommand = y_n_question("Found existing data files. Do you want to read data from them?")

        if command.action == ACTION_QUIT:
            return
        elif command.action == ACTION_YES:
            type = input("pickle or csv?\n")
            if type == "pickle":
                data = file_io.read_pickle()
            elif type == "csv":
                data = file_io.read_csv()

    print_collection_table(data, "Surname", "Candidate")

    winner = get_winner(data)
    if winner is not None:
        print("Winner:")
        print_collection_table({winner.surname: winner}, "Surname", "Vote Count")
    else:
        print("No winner\n")

    while True:
        surname = input("Find candidate by surname (q for quit, a for add, d for display, s for save)\n")
        if surname == "q":
            break
        elif surname == "d":
            print_collection_table(data, "Surname", "Candidate")
            continue
        elif surname == "s":
            type = input("pickle or csv?\n")
            if type == "pickle":
                file_io.write_pickle(data)
            elif type == "csv":
                file_io.write_csv(data)

            continue
        elif surname == "a":
            surname = input("Candidate surname: ")
            try:
                vote_count = int(input("Candidate vote count: "))
            except Exception:
                print("invalid vote count")
                continue

            data[surname] = Candidate(surname, vote_count)

        if surname in data:
            print(f"{surname}: {data.get(surname).vote_count}")


def get_winner(data: dict[str, Candidate]) -> Candidate:
    """
    Function returns candidate that wone more than one third of all votes
    (2000) or None if multiple/none won
    """
    res: list[Candidate] = []

    for _, candidate in data.items():
        print(candidate.surname, candidate)
        if float(candidate.vote_count) > TOTAL_VOTES/3:
            res.append(candidate)

    if len(res) == 1:
        return res[0]

    return None
