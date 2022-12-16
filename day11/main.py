from typing import List
import heapq
import math
import operator

# Map string representations of operators to functions in the operator module
op_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
}


class Monkey:
    def __init__(self, items: List[int], operation, testing) -> None:
        self.items = items
        self.operation = operation
        self.testing = testing
        self.inspected = 0

    def receive(self, item):
        self.items.append(item)

    def inspect(self):
        self.inspected += 1
        wl = self.items.pop(0)
        wl = self.operation(wl)
        wl //= 3
        return self.testing(wl), wl


def create_operation(a, op, b):
    if a == b:
        def function(old):
            return op_map[op](old, old)
        return function
    else:
        def function(old):
            return op_map[op](old, int(b))
        return function


def create_testing(div, true_target, false_target):
    def testing(x):
        return true_target if x % div == 0 else false_target
    return testing


monkeys = []

if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read().splitlines()

    for i in range(0, len(raw)+1, 7):
        # Get starting items with int.
        starting_items = raw[i+1][raw[i+1].find(":")+2:]
        starting_items = list(map(int, starting_items.split(", ")))

        # Get the worry level operation.
        new, _, a, op, b = raw[i+2][raw[i+2].find(":")+2:].split(" ")
        operation = create_operation(a, op, b)

        # Get the number that asking if divisible.
        testing_number = int(raw[i+3][-2:])
        true_target = int(raw[i+4][-1])
        false_target = int(raw[i+5][-1])
        testing = create_testing(testing_number, true_target, false_target)

        # define Monkey obj.
        m = Monkey(starting_items, operation, testing)
        monkeys.append(m)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                m, wl = monkey.inspect()
                monkeys[m].receive(wl)

    inspected = [m.inspected for m in monkeys]
    first_result = math.prod(heapq.nlargest(2, inspected))
    print(f"Part 1: {first_result}")
