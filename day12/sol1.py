# Richard Qiu
# Advent of Code 2020, Day 12

import numpy as np


def main():
    sin = lambda x: np.sin(np.deg2rad(x))
    cos = lambda x: np.cos(np.deg2rad(x))

    angle = [0]
    coords = np.array([[0.0], [0.0]])
    angles = {
        "N": [90],
        "E": [0],
        "S": [270],
        "W": [180],
        "F": angle
    }

    with open("input.txt", "r") as f:
        lines = [(line[0], int(line[1:])) for line in f.read().splitlines()]

    for direction, num in lines:
        if direction == "L":
            angle[0] = (angle[0] + num) % 360
        elif direction == "R":
            angle[0] = (angle[0] - num) % 360

        else:
            coords += num * np.array([cos(angles[direction]), sin(angles[direction])])

    return int(round(np.linalg.norm(coords, ord=1)))


if __name__ == "__main__":
    print(main())
