'''Day 23 solution'''
import sys
import itertools


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        data = [int(val) for val in input_f.read().strip('\n')]
        # data = input_f.read().split('\n\n')

    # create and return data structure
    return data


def main(input_f_name):
    '''The main function'''
    data_struct = parse_input(input_f_name)
    max_val = max(data_struct)
    min_val = min(data_struct)
    cur_val = data_struct[0]
    data_len = len(data_struct)
    print(data_struct, max_val, cur_val)
    # cir_iter = itertools.cycle(data_struct)
    for indx, ele in enumerate(data_struct):
        ahead = data_struct[indx + 1: data_len]
        behind = data_struct[0: indx]
        print(ele, ahead, behind)


if __name__ == '__main__':
    main(sys.argv[1])
