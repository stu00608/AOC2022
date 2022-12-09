import numpy as np
from typing import List


def get_distance(target: int, vision: List[int]):
    """Given tree target, and its sight from one direction,
    calculate how many tree it can see from target. Return
    the amount of visible tree.

    Parameters
    ----------
    target : int
        The center target.
    vision : List[int]
        The sight from one direction.

    Return
    ------
    int
        The amount of trees that are visible.
    """
    count = 0
    for item in vision:
        count += 1
        if item >= target:
            break
    return count


def visible_check(target: int, vision: List[int]):
    """Given tree target, and its sight from one direction,
    calculate if the tree is visible from outside by checking
    if there is any tree height >= target height.

    Parameters
    ----------
    target : int
        The center target.
    vision : List[int]
        The sight from one direction.

    Return
    ------
    bool
        Whether it's visible from current direction.
    """
    for item in vision:
        if item >= target:
            return False
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        tree_map = []
        for line in f:
            line = list(map(int, line.rstrip('\n')))
            tree_map.append(line)
        tree_map = np.array(tree_map)

    # Calculate the amount of elements around the matrix.
    size = len(tree_map)
    around = size**2 - (size-2)**2 if size > 2 else size ** 2
    print(around)
    # print(tree_map[1:-1, 1:-1])

    first_result = around
    for i in range(1, len(tree_map)-1):
        for j in range(1, len(tree_map[i])-1):
            is_visible = visible_check(tree_map[i, j], tree_map[i, 0:j]) |\
                visible_check(tree_map[i, j], tree_map[i, j+1:size]) |\
                visible_check(tree_map[i, j], tree_map[0:i, j]) |\
                visible_check(tree_map[i, j], tree_map[i+1:size, j])

            first_result += 1 if is_visible else 0

    second_result = 0
    for i in range(len(tree_map)):
        for j in range(len(tree_map[i])):
            visible_trees = get_distance(tree_map[i, j], list(reversed(tree_map[i, 0:j]))) *\
                get_distance(tree_map[i, j], tree_map[i, j+1:size]) *\
                get_distance(tree_map[i, j], list(reversed(tree_map[0:i, j]))) *\
                get_distance(tree_map[i, j], tree_map[i+1:size, j])
            second_result = max(second_result, visible_trees)

    print(f"Part 1: {first_result}")
    print(f"Part 2: {second_result}")
