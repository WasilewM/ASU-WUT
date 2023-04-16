import sys
from directory_cleaner import DirectoryCleaner


def run(args: list) -> int:
    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    DirectoryCleaner(args[1]).run()
    return 0


if __name__ == "__main__":
    run(sys.argv)
