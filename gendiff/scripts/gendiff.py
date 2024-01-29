from gendiff.utils import parse_file, parse_args


def main():
    args = parse_args()

    file1 = parse_file(args.first_file)
    file2 = parse_file(args.second_file)

    print(set(file1) & set(file2))
    print(set(file1) ^ set(file2))


if __name__ == "__main__":
    main()
