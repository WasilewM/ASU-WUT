import os
import sys


def run(args):
    print("CWD: ", os.getcwd())


if __name__ == "__main__":
    run(sys.argv)