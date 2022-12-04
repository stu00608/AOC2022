if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()
    
    first_result = 0
    for data in data_list:
        first, second = data.split(",")

        start, end = first.split("-")
        range1 = set(range(int(start), int(end)+1))
        start, end = second.split("-")
        range2 = set(range(int(start), int(end)+1))
        short = min([range1, range2], key=len)
        if (range1 & range2) == short:
            first_result += 1
        

    print(f"Part 1: {first_result}")