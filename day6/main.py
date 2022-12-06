if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    history = set()
    for i, c in enumerate(data):
        if c in history:
            history = set(c)
        else:
            history.add(c)
        if len(history) == 4:
            break
    print(f"Part 1: {i+1}")
