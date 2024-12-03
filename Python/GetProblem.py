import urllib.request
import os


def get_problem_(day: int, year: int):
    save_path = f"../ProblemInputs/{year}-{day}.txt"
    try:
        with open(save_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        cookie_value = os.getenv("AOCCOOKIE")
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


def get_problem(day: 1, year: 2024):
    def decorator(part_function):
        # These function should not take arguments/kwargs
        def wrapper():
            return part_function(get_problem_(day, year))

        return wrapper

    return decorator


if __name__ == "__main__":
    get_problem(1, 2004)
