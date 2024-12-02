from GetProblem import get_problem

if __name__ == "__main__":
    foo = get_problem(1, 2024)

    # split the data number (string)
    left_and_rights = [line.split() for line in foo.split("\n") if len(line)]
    # Transpose the list
    left, right = map(list, zip(*left_and_rights))

    left = sorted([int(i) for i in left])
    right = sorted([int(i) for i in right])

    output = sum(abs(l - r) for l, r in zip(left, right))
    print(output)
