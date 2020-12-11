# Richard Qiu
# Advent of Code 2020, Day 11

from collections import defaultdict
from copy import deepcopy
from itertools import product

directions = set(product([-1, 0, 1], repeat=2))
directions.remove((0, 0))


def main():
    with open("input.txt", "r") as f:
        lines = [list(line) for line in f.read().splitlines()]

    visible_seats_dict = defaultdict(set)
    for i, line in enumerate(lines):
        for j, seat in enumerate(line):
            if seat == ".":
                continue
            for x_diff, y_diff in directions:
                x, y = i, j
                while True:
                    x += x_diff
                    y += y_diff
                    if x >= len(lines) or x < 0 or y >= len(line) or y < 0:
                        break
                    if lines[x][y] == "L":
                        visible_seats_dict[(i, j)].add((x, y))
                        break

    current_state = lines
    next_state = deepcopy(current_state)
    while True:
        for (i, j), visible_seats in visible_seats_dict.items():
            n_occupied = sum((current_state[x][y] == "#") for x, y in visible_seats)
            if current_state[i][j] == "#" and n_occupied >= 5:
                next_state[i][j] = "L"
            elif current_state[i][j] == "L" and n_occupied == 0:
                next_state[i][j] = "#"
            else:
                next_state[i][j] = current_state[i][j]

        if current_state == next_state:
            return sum(row.count("#") for row in current_state)
        else:
            current_state, next_state = next_state, current_state


if __name__ == "__main__":
    print(main())
