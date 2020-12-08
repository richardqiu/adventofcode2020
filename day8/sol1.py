# Richard Qiu
# Advent of Code 2020, Day 8


def main():
    with open("input.txt", "r") as f:
        lines = [line.split(" ") for line in f.read().splitlines()]

    visited = set()
    accumulator = 0
    idx = 0
    while True:
        if idx in visited:
            break

        visited.add(idx)
        instruction, val = lines[idx]
        if instruction == "acc":
            accumulator += int(val)
            idx += 1
        elif instruction == "jmp":
            idx += int(val)
        elif instruction == "nop":
            idx += 1

    print(accumulator)


if __name__ == "__main__":
    main()
