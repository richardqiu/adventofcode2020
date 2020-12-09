# Richard Qiu
# Advent of Code 2020, Day 9

preamble_len = 25


def main():
    print("SET TWO SUM")
    with open("input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    for i in range(preamble_len, len(lines)):
        if not has_twosum2(lines[i : i + preamble_len], lines[i + preamble_len]):
            return lines[i + preamble_len]


def has_twosum2(preamble, target):
    s = set()
    for n in preamble:
        if n in s:
            return True
        else:
            s.add(target - n)
    return False


if __name__ == "__main__":
    print(main())
