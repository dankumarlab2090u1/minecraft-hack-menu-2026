"""Entry point for toolkit."""

from utils import prepare


def main():
    result = prepare(20)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
