# Richard Qiu
# Advent of Code 2020, Day 11

import numpy as np
from scipy.signal import convolve2d


conv_filter = np.array(
    [
        [1, 1, 1],
        [1, -9, 1],
        [1, 1, 1],
    ]
)


def main():
    with open("input.txt", "r") as f:
        lines = [
            list(map(int, line.replace("L", "1").replace(".", "0")))
            for line in f.read().splitlines()
        ]

    valid_seats = np.array(lines)
    current_state = valid_seats.copy()
    i = 0
    while True:
        next_state = convolve2d(current_state, conv_filter, mode="same")
        next_state = np.where(np.logical_or(next_state <= -6, next_state == 0), 1, 0)
        next_state = np.multiply(valid_seats, next_state)


        if np.array_equal(current_state, next_state):
            return next_state.sum()
        else:
            current_state = next_state


if __name__ == "__main__":
    print(main())
