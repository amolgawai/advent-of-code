"""Day 20 solution"""
import sys


def parse_input(input_f_name):
    """parses input from the given file name and returns data"""
    with open(input_f_name) as input_f:
        data = input_f.read()
        # data = input_f.read().split('\n\n')

    # create and return data structure
    return data


def main(input_f_name):
    """The main function"""
    data_struct = parse_input(input_f_name)


if __name__ == "__main__":
    main(sys.argv[1])
