# Richard Qiu
# Advent of Code 2020, Day 7

from collections import defaultdict


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    global bag_graph
    bag_graph = defaultdict(list)
    for line in lines:
        outer_bag, inner_bags = line.split(" bags contain ")
        inner_bags = inner_bags.replace(".", "").split(", ")
        inner_bags = [
            bag.replace(" bags", "").replace(" bag", "").strip() for bag in inner_bags
        ]

        for inner_bag in inner_bags:
            if inner_bag == "no other":
                bag_count_tuple = (0, "no other")
            else:
                bag_count_tuple = (int(inner_bag[0]), inner_bag[2:])
            bag_graph[outer_bag].append(bag_count_tuple)

    # Subtract golden bag itself
    print(dfs_subroutine("shiny gold") - 1)


# Assume DAG
def dfs_subroutine(bag):
    global bag_graph
    if bag == "no other":
        return 1

    n_inner_bags = [
        inner_bag[0] * dfs_subroutine(inner_bag[1]) for inner_bag in bag_graph[bag]
    ]

    # Count outer bag too
    return sum(n_inner_bags) + 1


if __name__ == "__main__":
    main()
