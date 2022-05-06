#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{len(argv) - 1} arguments:")
        for count, i in enumerate(argv):
            if i != argv[0]:
                print(f"{count}: {i}")


if __name__ == "__main__":
    main()
