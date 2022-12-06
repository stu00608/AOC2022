def get_marker(data: str, genre: int):
    """

    Parameters
    ----------
    data : str
        Data stream.
    genre : int
        The amount that require to consider as a marker.
    """

    history = set()
    for i in range(len(data)-genre):
        if len(set(data[i:i+genre])) == genre:
            return i + genre


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    first_result = get_marker(data, 4)
    second_result = get_marker(data, 14)
    print(f"Part 1: {first_result}")
    print(f"Part 2: {second_result}")
