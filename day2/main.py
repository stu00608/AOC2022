mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}


def rps_checking(oppo: int, pick: int):
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

def rps_checking_inverse(oppo: int, cond: int):
    """Return the selection by 

    Parameters
    ----------
    oppo : int
        The opponent selection. 0 for Rock, 1 for Paper, 2 for Scissor.
    cond : 
        Condition, 0 for seeking lose, 1 for draw, 2 for win.
    
    Return
    ------
    int
        the selection for specified condition, 0 for Rock, 1 for Paper, 2 for Scissor
    """
    if cond == 0:
        return (oppo - 1) % 3
    elif cond == 1:
        return oppo
    else:
        return (oppo + 1) % 3

if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()
    total_score_part_1 = 0
    total_score_part_2 = 0
    for data in data_list:
        oppo, pick = data.split(' ')
        oppo, pick = mapping[oppo], mapping[pick]
        total_score_part_1 += rps_checking(oppo, pick) + pick + 1
        total_score_part_2 += pick * 3 + rps_checking_inverse(oppo, cond=pick) + 1
    print(f"Part 1: {total_score_part_1}")
    print(f"Part 2: {total_score_part_2}")

    
    