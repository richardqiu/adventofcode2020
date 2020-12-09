# Richard Qiu
# Advent of Code 2020, Day 9

from collections import deque

from sol1 import main as sol1


def main():
    with open("input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    bad_n = sol1()

    queue = deque([lines[0]])
    queue_sum = lines[0]
    right_idx = 1
    while True:
        if queue_sum < bad_n:
            queue.append(lines[right_idx])
            queue_sum += queue[-1]
            right_idx += 1
        elif queue_sum > bad_n:
            queue_sum -= queue.popleft()
        else:
            return min(queue) + max(queue)


if __name__ == "__main__":
    print(main())
