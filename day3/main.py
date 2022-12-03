def compare(*candidate):
    """Compare strings, find the one char that appear in all strings."""
    for c in min(*candidate, key=len):
        state_list = [c in can for can in candidate[0]]
        if False in state_list:
            continue
        else:
            return c
    return None

def get_priority(c: str):
    """Given char return its priority by following rule, a-z:1-26, A-Z:27-52"""
    assert len(c) == 1
    if c.islower():
        return ord(c) - 97 + 1
    elif c.isupper():
        return ord(c) - 65 + 27

if __name__ == "__main__":
    with open("input.txt") as f:
        data_list = f.read().splitlines()
    
    priority_list = []
    for data in data_list:
        first, second = data[:len(data)//2], data[len(data)//2:]
        item = compare([first, second])
        priority = get_priority(item)
        priority_list.append(priority)
    print(f"Part 1: {sum(priority_list)}")
    

