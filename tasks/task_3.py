import matplotlib.pyplot as plt
import math
import core.io as io
import numpy as np


class MathClass:
    @staticmethod
    def taylor(x: float, n: int) -> float:
        return 2/((2*n + 1) * x ** (2*n + 1))

    @staticmethod
    def task_3():
        print("What graph to build?\n1)Graph and Taylor polynomial approximation\n2)epsylon from n\n3)mean, mode etc.")
        while True:
            ans = io.input_int()
            if ans == 1:
                MathClass.plot_function_graphs()
                return
            elif ans == 2:
                MathClass.plot_epsilon_from_n()
                return
            elif ans == 3:
                MathClass.statistics_metrics()
                return
            else:
                print("wrong option")

    @staticmethod
    def statistics_metrics():
        print("Input number of taylor iterations")
        n = io.input_int()

        print("Input number of points to analyze")
        points = io.input_int()

        step = 1/points

        taylor_points = []

        x = 2.0
        while x < 3:
            taylor_sum = 0
            for i in range(n):
                taylor_sum += MathClass.taylor(x, i)

            taylor_points.append(taylor_sum)
            x += step

        print(f"Mean: {np.mean(taylor_points)}")
        print(f"Median: {np.median(taylor_points)}")

        mode = 0
        mode_count = 0
        taylor_mode_dict = {}
        for val in taylor_points:
            if taylor_mode_dict.get(val) is None:
                taylor_mode_dict[val] = 1
            else:
                taylor_mode_dict[val] += 1

        for val, count in taylor_mode_dict.items():
            if count > mode_count:
                mode = val
                mode_count = count

        print(f"Mode: {mode} (count: {mode_count})")
        print(f"Variance: {np.var(taylor_points)}")
        print(f"Standard deviation: {np.std(taylor_points)}")

    @staticmethod
    def plot_epsilon_from_n():
        eps_vals = []
        n_vals = []
        x = 2.0

        print("Input number of taylor iterations")
        n = io.input_int()

        for i in range(n):
            taylor_sum = 0
            for j in range(i):
                taylor_sum += MathClass.taylor(x, j)

            mth = math.log((x+1)/(x-1))
            print(f"Taylor: {taylor_sum}\nMath: {mth}")
            n_vals.append(i)
            eps_vals.append(abs(taylor_sum - mth))

        plt.bar(n_vals, eps_vals, color="blue")
        plt.show()

    @staticmethod
    def plot_function_graphs():
        x = 2.0

        print("Input number of taylor iterations")
        n = io.input_int()

        print("Input number of points to plot")
        points = io.input_int()

        step = 1/points

        x_vals = []
        math_points = []
        taylor_points = []

        while x < 3:
            x_vals.append(x)
            taylor_sum = 0
            for i in range(n):
                taylor_sum += MathClass.taylor(x, i)

            taylor_points.append(taylor_sum)
            math_points.append(math.log((x+1)/(x-1)))
            x += step

        plt.plot(x_vals, math_points, color="blue", label="math lib")
        plt.plot(x_vals, taylor_points, color="red", label="taylor")
        plt.axis((2, 3, math_points[0], math_points[-1]))
        plt.show()
