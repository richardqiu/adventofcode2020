# Richard Qiu
# Advent of Code 2020, Day 8


def main():
    with open("input.txt", "r") as f:
        lines = [line.split(" ") for line in f.read().splitlines()]

    for i in range(len(lines)):
        if lines[i][0] == "acc":
            continue

        lines[i][0] = "nop" if lines[i][0] == "jmp" else "jmp"

        accumulator = check_instructions_valid(lines)
        if accumulator:
            print(accumulator)
            break
        else:
            lines[i][0] = "nop" if lines[i][0] == "jmp" else "jmp"


def check_instructions_valid(instructions):
    visited = set()
    accumulator = 0
    idx = 0
    while True:
        if idx in visited:
            return False
        elif idx == len(instructions):
            return accumulator

        visited.add(idx)
        instruction, val = instructions[idx]
        if instruction == "acc":
            accumulator += int(val)
            idx += 1
        elif instruction == "jmp":
            idx += int(val)
        elif instruction == "nop":
            idx += 1


if __name__ == "__main__":
    main()
