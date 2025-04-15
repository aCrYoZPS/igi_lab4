import numpy as np
import random


def task_5():
    n, m = 3, 2
    narr = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(random.randint(0, 100))
        narr.append(row)

    A = np.array(narr)
    print(A)
    pass
