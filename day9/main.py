import numpy as np
import math

if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()

    h_pos = last_h_pos = [0, 0]
    t_pos = [0, 0]

    t_path = [[0, 0]]
    map = np.array([['*']*7]*7)
    for item in data_list:
        direction, step = item.split(" ")

        for i in range(int(step)):

            if direction == 'R':
                h_pos[0] += 1
            elif direction == 'U':
                h_pos[1] += 1
            elif direction == 'L':
                h_pos[0] -= 1
            elif direction == 'D':
                h_pos[1] -= 1

            if math.dist(t_pos, h_pos) > math.sqrt(2):
                t_pos = last_h_pos.copy()
                if not t_pos in t_path:
                    t_path.append(t_pos)

            temp_map = map.copy()
            # print(direction, step)
            # print(f"How many point t passed: {len(t_path)}")
            # print("=======================")
            # temp_map[h_pos[0], h_pos[1]] = 'H'
            # temp_map[t_pos[0], t_pos[1]] = 'T'
            # print(temp_map[:, ::-1].T)
            # print("=======================")

            last_h_pos = h_pos.copy()

    print(f"Part 1: {len(t_path)}")
