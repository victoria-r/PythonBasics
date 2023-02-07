#!/usr/bin/env python3
# basic_classes.py
"""Python script showing examples of basic classes and their stucture"""

import math


class Circle:
    """Circle class"""


    def __init__(self, color, radius):
        """Attributes"""
        self.color = color.lower()
        self.radius = radius


    def diameter(self):
        """Calculates the diameter of the circle"""
        return 2 * self.radius


    def circumfrence(self):
        """Calculates the circumfrence of the circle"""
        return 2 * math.pi * self.radius



    def isRed(self):
        """Returns true is the circle is red"""
        return bool(self.color == "red")


class GraduateStudent:
    """GraduateStudent class"""


    def __init__(self, first_name=str, last_name=str, year=int, major=str):
        """Attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major


    def year_matriculated(self):
        """Returns the year that the student began studying"""
        return 2021 - self.year


if __name__ == '__main__':

    # Circle class example instances
    circle_1 = Circle("Red", 20)
    circle_2 = Circle("Blue", 30)

    # Circle class method functionality examples
    print(f"The diameter of circle_1 is: {circle_1.diameter()}")
    print(f"Is circle_1 red? {circle_1.isRed()}")
    print(f"The circumfrence of circle_2 is: {circle_2.circumfrence()}")
    print(f"Is circle_2 red? {circle_2.isRed()}")

    # GraduateStudent class example instaces
    student_1 = GraduateStudent("Jane", "Doe", 1, "Bioinformatics")
    student_2 = GraduateStudent("John", "Dough", 5, "Biology")

    # GraduateStuden class method functionality examples
    print(f"What year did student_1 matriculate? {student_1.year_matriculated()}")
    print(f"What year did student_2 matriculate? {student_2.year_matriculated()}")
