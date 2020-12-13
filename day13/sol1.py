# Richard Qiu
# Advent of Code 2020, Day 13


def main():

    with open("input.txt", "r") as f:
        arrival_time, buses = f.read().splitlines()

    arrival_time = int(arrival_time)
    buses = [int(bus) for bus in buses.split(",") if bus != "x"]

    wait_times = [(bus - (arrival_time % bus), bus) for bus in buses]
    min_wait = min(wait_times)
    return min_wait[0] * min_wait[1]


if __name__ == "__main__":
    print(main())
