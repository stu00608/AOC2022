if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = []
        data = []
        for line in f:
            if line == '\n':
                data_list.append(sum(data))
                data = []
            else:
                data.append(int(line.rstrip('\n')))

    print(f"Part1 : {max(data_list)}")
    print(f"Part2 : {sum(sorted(data_list, reverse=True)[:3])}")
