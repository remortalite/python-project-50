import argparse

from gendiff.utils import parse_file


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()

    file1 = parse_file(args.first_file)
    file2 = parse_file(args.second_file)

    print(set(file1) & set(file2))
    print(set(file1) ^ set(file2))


if __name__ == "__main__":
    main()
