# Richard Qiu
# Advent of Code 2020, Day 6

from string import ascii_lowercase

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        lines.append("")

    n_yeses = 0
    group_yeses = set(ascii_lowercase)
    for line in lines:
        if line == "":
            n_yeses += len(group_yeses)
            group_yeses = set(ascii_lowercase)
        else:
            group_yeses = group_yeses.intersection(set(list(line)))

    print(n_yeses)


if __name__ == "__main__":
    main()
