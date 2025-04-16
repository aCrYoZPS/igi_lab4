from core.globals import ACTION_NO, ACTION_QUIT, ACTION_YES

actions_dict: dict[str, int] = {"q": ACTION_QUIT, "y": ACTION_YES,
                                "n": ACTION_NO}


class IOCommand:
    def __init__(self, action: int):
        self.action = actions_dict.get(action)


def y_n_question(prompt: str) -> IOCommand:
    inpt = ""
    while True:
        inpt = input(f"{prompt} [Y] - Yes, [N] - No, [Q] - Quit\n")
        inpt = inpt.lower()
        if (inpt in "ynq"):
            return IOCommand(inpt)


def print_collection_table(collection, col1_name: str = "Key",
                           col2_name: str = "Value"):
    """
    Prints a table representing a collection.

    Args:
        collection: The collection to display (dict, list, set, etc.)
        col1_name: Header for first column (default "Key")
        col2_name: Header for second column (default "Value")
    """

    max_key_len = len(col1_name)
    max_val_len = len(col2_name)

    items = []
    if isinstance(collection, dict):
        items = collection.items()
    elif isinstance(collection, (list, tuple, set)):
        items = [(i, item) for i, item in enumerate(collection)]
    else:
        raise ValueError("Unsupported collection type")

    for key, value in items:
        max_key_len = max(max_key_len, len(str(key)))
        max_val_len = max(max_val_len, len(str(value)))

    header = f"| {col1_name.ljust(max_key_len)} | {col2_name.ljust(max_val_len)} |"
    separator = "+-" + "-" * max_key_len + "-+-" + "-" * max_val_len + "-+"

    print(separator)
    print(header)
    print(separator)

    for key, value in items:
        row = f"| {str(key).ljust(max_key_len)} | {str(value).ljust(max_val_len)} |"
        print(row)

    print(separator)


def input_int() -> int:
    """
    Function that takes user input and checks it
    :returns: correct whole number
    """
    while True:
        input_str = input("Input a number: ")
        res = 0
        try:
            res = int(input_str)
            break
        except ValueError:
            print("Invalid input. Input whole number: ")

    return res


def input_float() -> float:
    """
    Function that takes user input and checks it
    :returns: correct floating point number
    """
    while True:
        input_str = input("Input a number: ")
        res = 0.0
        try:
            res = float(input_str)
            break
        except ValueError:
            print("Invalid input. Input correct real number: ")

    return res


def input_int_arr(predicate):
    """
    Function that returns a list of integers from stdinput
    """
    result = []
    while True:
        elem = input_int()

        if not predicate(elem):
            return result

        result.append(elem)


def gen_floats(n: int):
    count = 0
    while count < n:
        yield input_int()
        count += 1


def show_menu() -> int:
    while True:
        menu_intro = "Lab Work #4. Choose a task (1-5)," + " 6 for quit"
        print(menu_intro)

        n = input_int()
        if n > 6 or n < 1:
            print("Invalid option")
            continue

        return n
