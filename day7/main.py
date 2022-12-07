import os
from os.path import join, dirname

if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()
        data_list = list(reversed(data_list))

    record = {'/': 0}
    current_path = '/'
    while data_list:
        data = data_list.pop()
        if data[0] == '$':
            if data[2:4] == "cd":
                _, cd, dest = data.split(" ")
                if dest == '..':
                    current_path = dirname(current_path)
                elif dest == '/':
                    current_path = '/'
                else:
                    current_path = join(current_path, dest)
        else:
            indicator, name = data.split(" ")
            if indicator == "dir":
                record[join(current_path, name)] = 0
            else:
                record[current_path] += int(indicator)
                temp_path = current_path
                while dirname(temp_path) != temp_path:
                    record[dirname(temp_path)] += int(indicator)
                    temp_path = dirname(temp_path)

    folder_size_list = list(record.values())
    first_result = sum(item for item in folder_size_list if item <= 100000)

    print(f"Part 1: {first_result}")

    sorted_folder_size_list = sorted(folder_size_list)

    required_space = abs(record["/"] - 70000000)
    required_space = 30000000 - required_space
    for item in sorted_folder_size_list:
        if item >= required_space:
            print(f"Part 2: {item}")
            break
