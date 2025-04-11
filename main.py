import core.file_io as file_io
import core.io as io
from entities.candidate import Candidate


def main():
    candidates: list[Candidate] = []

    candidates.append(Candidate("Ivanov", 10))
    candidates.append(Candidate("Petrov", 20))
    candidates.append(Candidate("Sidorov", 5))

    candidates_dict: dict[str, Candidate] = {}

    for candidate in candidates:
        candidates_dict[candidate.surname] = candidate

    file_io.write_csv(candidates_dict)
    file_io.write_pickle(candidates_dict)

    dict2 = file_io.read_csv()
    io.print_collection_table(dict2, "Candidate", "Vote count")


if __name__ == "__main__":
    main()
