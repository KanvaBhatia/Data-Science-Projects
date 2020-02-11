"""
    # 3_triangle_area.py
    # This program computes the area of a triangle via the length of its sides a, b, c
    Created by: temikelani on: 1/30/20
"""

import math


def area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main(a, b, c):
    print("the area is", area(a, b, c))


main(3, 4, 5)
