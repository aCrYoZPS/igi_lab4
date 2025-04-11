class Candidate:
    def __init__(self, surname: str, vote_count: int):
        self.surname = surname
        self.vote_count = vote_count

    def __str__(self) -> str:
        return f"{self.vote_count}"
