import sys
from test_files_creator import TestFilesCreator


def run(args):
    tem = TestFilesCreator()
    tem.prepare_env()


if __name__ == "__main__":
    run(sys.argv)
