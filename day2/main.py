mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}


def rps_checking(pick: int, oppo: int):
    """Check if Rock Paper Scissor win, draw or lose.

    Parameters
    ----------
    pick : int
        The player selection. 0 for Rock, 1 for Paper, 2 for Scissor.
    oppo : int
        The opponent selection. 0 for Rock, 1 for Paper, 2 for Scissor.
    
    Return
    ------
    int
        0 for lose, 3 for draw, 6 for win. 
    """
    if (pick + 1) % 3 == oppo:
        return 0
    elif pick == oppo:
        return 3
    else:
        return 6


if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()
    total_score = 0
    for data in data_list:
        oppo, pick = data.split(' ')
        total_score += rps_checking(mapping[pick], mapping[oppo]) + mapping[pick] + 1
    print(f"Part 1: {total_score}")

    
    