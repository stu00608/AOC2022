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

        command_list = f.read().splitlines()
    return stacks, command_list


if __name__ == "__main__":
    line = 1
    stacks, command_list = get_inputs("input.txt")
    for command in command_list:
        _, count, _, src, _, dest = command.split(" ")
        count = int(count)
        src = int(src) - 1
        dest = int(dest) - 1

        for i in range(count):
            item = stacks[src].pop()
            stacks[dest].append(item)

    first_result = ""
    for stack in stacks:
        first_result += stack[-1][1]

    print(f"Part 1: {first_result}")
