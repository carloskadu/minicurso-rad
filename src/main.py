import sys


def run(message: str) -> int:
    print(message)
    return 0


def main():
    message = "Iris Reld"
    sys.exit(run(message))


if __name__ == "__main__":
    main()
