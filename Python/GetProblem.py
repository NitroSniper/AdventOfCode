import urllib.request


def get_problem(day: int, year: int):
    save_path = f"../ProblemInputs/{year}-{day}.txt"
    try:
        with open(save_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        cookie_value = ""
        request = urllib.request.Request(
            f"https://adventofcode.com/{year}/day/{day}/input"
        )
        request.add_header("Cookie", f"session={cookie_value}")
        with urllib.request.urlopen(request) as r:
            with open(save_path, "wb") as f:
                content = r.read()
                f.write(content)
        content = content.decode()
    finally:
        return content


if __name__ == "__main__":
    get_problem(1, 2004)
