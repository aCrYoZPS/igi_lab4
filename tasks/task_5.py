import numpy as np
import random
import math
from core.io import input_int


def standard_deviation(sequence) -> float:
    mean = sum(sequence)/len(sequence)
    sum_squares = 0
    for element in sequence:
        sum_squares += (element - mean)**2

    return math.sqrt(sum_squares/len(sequence))


def task_5():
    print("Input number of columns")
    n = input_int()
    print("Input number of rows")
    m = input_int()
    narr = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(random.randint(-100, 100))
        narr.append(row)

    A = np.array(narr)
    print(A)

    neg_odd_elems = []

    for elem in np.nditer(A):
        if elem < 0 and elem % 2 == 1:
            neg_odd_elems.append(elem)

    abs_sum = 0
    for elem in neg_odd_elems:
        abs_sum += abs(elem)

    print(f"Sum of absolute values of negative odd elements: {abs_sum}")
    print(f"Numpy standard deviation: {np.std(neg_odd_elems):.2f}")
    print(f"Computed standard deviation: {standard_deviation(neg_odd_elems):.2f}")
