from GetProblem import get_problem
from collections import Counter


def part_1() -> None:
    foo = get_problem(1, 2024)
    # split the data number (string)
    left_and_rights = [line.split() for line in foo.split("\n") if len(line)]

    # Transpose the list
    left, right = map(list, zip(*left_and_rights))

    left = sorted([int(i) for i in left])
    right = sorted([int(i) for i in right])

    output = sum(abs(l - r) for l, r in zip(left, right))
    return output


def part_2() -> None:
    foo = get_problem(1, 2024)
    # split the data number (string)
    left_and_rights = [line.split() for line in foo.split("\n") if len(line)]
    # Transpose the list
    left, right = map(list, zip(*left_and_rights))

    left = sorted([int(i) for i in left])
    right = Counter([int(i) for i in right])

    output = sum(l * right[l] for l in left)
    return output


if __name__ == "__main__":
    print(part_2())
