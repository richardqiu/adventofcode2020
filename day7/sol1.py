# Richard Qiu
# Advent of Code 2020, Day 7

from collections import defaultdict


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    bag_graph = defaultdict(list)
    for line in lines:
        outer_bag, inner_bags = line.split(" bags contain ")
        inner_bags = "".join(c for c in inner_bags if not c.isdigit())
        inner_bags = inner_bags.replace(".", "").split(", ")
        inner_bags = [
            bag.replace(" bags", "").replace(" bag", "").strip() for bag in inner_bags
        ]

        [bag_graph[inner_bag].append(outer_bag) for inner_bag in inner_bags]

    # standard DFS
    visited = set()
    stack = ["shiny gold"]
    while stack:
        node = stack.pop()
        visited.add(node)
        stack.extend(bag_graph[node])

    print(len(visited) - 1)


if __name__ == "__main__":
    main()
