import copy
import numpy as np


def get_inputs(filename: str):
    """Given filename, read the stack matrix and command list."""
    line = 1
    data_list = []
    with open("input.txt") as f:
        # Reading table.
        while line != '':
            line = f.readline().rstrip('\n')
            data_list.insert(0, line)
        data_list = data_list[2:]

        stacks = [[] for _ in range(9)]
        for row in data_list:
            for i in range(len(row)):
                item = row[i*4:i*4+3]
                if item.isspace() or item == "":
                    continue
                else:
                    stacks[i].append(item)
            print(row)
        command_list = f.read().splitlines()
    return stacks, command_list


def get_result(stacks):
    result = ""
    for stack in stacks:
        result += stack[-1][1]
    return result


if __name__ == "__main__":
    line = 1
    stacks, command_list = get_inputs("input.txt")
    stacks_1, stacks_2 = copy.deepcopy(stacks), copy.deepcopy(stacks)
    del stacks

    for command in command_list:
        _, count, _, src, _, dest = command.split(" ")
        count = int(count)
        src = int(src) - 1
        dest = int(dest) - 1

        # For part 1
        for i in range(count):
            item = stacks_1[src].pop()
            stacks_1[dest].append(item)

        # For part 2
        stacks_2[dest] += stacks_2[src][-count:]
        stacks_2[src] = stacks_2[src][:-count]

    result_1 = get_result(stacks_1)
    result_2 = get_result(stacks_2)

    print(f"Part 1: {result_1}")
    print(f"Part 2: {result_2}")
