if __name__ == "__main__":
    with open("input.txt") as f:
        commands = f.read().splitlines()

    cycle_history = {}
    cycle = 1
    x = 1
    for command in commands:
        if command.startswith("addx"):
            cmd, val = command.split(" ")
            cycle_history[cycle] = x
            x += int(val)
            cycle += 1
            cycle_history[cycle] = x
            cycle += 1
        else:
            cycle_history[cycle] = x
            cycle += 1
    print(cycle_history)

    target_round = [20, 60, 100, 140, 180, 220]
    first_result = 0
    for target in target_round:
        first_result += target*cycle_history[target-1]

    print(f"Part 1: {first_result}")
