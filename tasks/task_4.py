from abc import ABC, abstractmethod
import re
import math
import matplotlib.pyplot as plt
import numpy as np
from core.io import input_float


color_regex = r"^#?([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$"


class Color():
    def __init__(self):
        self.__color = None

    def set_color(self, hex_color: str):
        if re.match(color_regex, hex_color):
            self.__color = hex_color
        else:
            raise ValueError("Invalid hex color")

    def get_color(self):
        return self.__color

    def del_color(self):
        del self.__color

    color = property(get_color, set_color, del_color)


class Figure(ABC):
    def __init__(self, hex_color: str):
        self.color = Color()
        try:
            self.color.color = hex_color
        except ValueError:
            self.color.color = "#000000"

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Parallelogram(Figure):
    info_format: str = "Parallelogram:\nDiagonal 1: {d1:.2f}\n" \
        + "Diagonal 2: {d2:.2f}\nAngle {angle:.2f}\nArea: {area:.2f}\n" \
        + "Color: {color}"

    def __init__(self, d1: float, d2: float, angle: float, hex_color: str):
        super().__init__(hex_color)
        self.d1 = d1
        self.d2 = d2
        self.angle = angle * math.pi / 180

    def calculate_area(self):
        return 0.5 * self.d1 * self.d2 * math.sin(self.angle)

    def draw(self):
        half_d1 = self.d1 / 2
        half_d2 = self.d2 / 2

        v1 = np.array([half_d1, 0])

        v2 = np.array([half_d2 * np.cos(self.angle), half_d2 * np.sin(self.angle)])

        A = v1 + v2
        B = -v1 + v2
        C = -v1 - v2
        D = v1 - v2

        vertices = np.array([A, B, C, D])

        fig, ax = plt.subplots()
        parallelogram = plt.Polygon(vertices,
                                    closed=True,
                                    edgecolor=self.color.color,
                                    facecolor=self.color.color,
                                    alpha=0.7)
        ax.add_patch(parallelogram)

        max_dim = max(self.d1, self.d2)
        ax.set_xlim(-max_dim, max_dim)
        ax.set_ylim(-max_dim, max_dim)
        ax.set_aspect('equal')
        ax.grid(True)

        plt.title(f"Parallelogram\nDiagonals: {self.d1}, {self.d2};" +
                  f" Angle: {np.degrees(self.angle):.2f}°")

        plt.show()

    def __str__(self):
        data = {"d1": self.d1,
                "d2": self.d2,
                "angle": self.angle,
                "area": self.calculate_area(),
                "color": self.color.color}

        return Parallelogram.info_format.format(**data)


def task_4():
    print("Input first diagonal:")
    d1 = input_float()
    print("Input second diagonal:")
    d2 = input_float()

    print("Input angle (in degrees):")
    angle = input_float()

    color = input("Input hex color:\n")

    if angle > 90:
        print("Invalid angle")
        return

    par = Parallelogram(d1, d2, angle, color)
    par.draw()
