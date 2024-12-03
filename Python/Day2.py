from GetProblem import get_problem


@get_problem(2, 2024)
def part_1(input_data) -> None:
    def per_case(line):
        numbers = [int(number_str) for number_str in line.split()]
        differences = [i - j for i, j in zip(numbers[:-1], numbers[1:])]
        # Either True, None, False (True for ascending, False for descending)
        order = set(x > 0 if x else None for x in differences)

        # This filter out if 0 in the line and if it's not in order
        if len(order) > 1:
            return False

        (is_ascending,) = order  # get the single element

        # Order it depending if it is ascending and descending so the highest magnitude number is at the front
        differences.sort(reverse=is_ascending)

        return abs(differences[0]) <= 3

    return sum(1 for line in input_data.split("\n") if line and per_case(line))


@get_problem(2, 2024)
def part_2(input_data) -> None:
    pass


if __name__ == "__main__":
    print(part_1())
