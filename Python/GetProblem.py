import urllib.request


def get_problem(day: int, year: int):
    save_path = "../ProblemInputs/foo.txt"
    with open(save_path, "r") as f:
        content = f.read()
    return content
    cookie_value = ""
    request = urllib.request.Request("https://adventofcode.com/2024/day/1/input")
    request.add_header("Cookie", f"session={cookie_value}")

    with urllib.request.urlopen(request) as r:
        with open(save_path, "wb") as f:
            content = r.read()
            f.write(content)


if __name__ == "__main__":
    get_problem(1, 2004)
