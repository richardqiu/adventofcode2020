# Richard Qiu
# Advent of Code 2020, Day 10


def main():
    with open("input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()

    chargers = {line: 0 for line in lines}
    chargers[0] = 1

    for n in lines:
        for i in range(1, 4):
            if n + i in chargers:
                chargers[n + i] += chargers[n]

    return chargers[max(lines)]


if __name__ == "__main__":
    print(main())
