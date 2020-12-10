# Richard Qiu
# Advent of Code 2020, Day 10


def main():
    with open("input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    n_1gaps = 0
    n_3gaps = 0
    for n1, n2 in zip(lines[:-1], lines[1:]):
        diff = n2 - n1
        if diff == 3:
            n_3gaps += 1
        elif diff == 1:
            n_1gaps += 1

    return n_1gaps * n_3gaps


if __name__ == "__main__":
    print(main())
