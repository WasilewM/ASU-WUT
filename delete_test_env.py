import sys
from test_env_manager import TestEnvManager


def run(args):
    tem = TestEnvManager()
    tem.delete_env()


if __name__ == "__main__":
    run(sys.argv)