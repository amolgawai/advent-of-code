'''Day 21 solution'''
import sys
import re

patrn = re.compile(r'\((contains .*)\)')


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        data = [tuple(filter(None, patrn.split(ln.strip('\n'))))
                for ln in input_f.readlines()]

    aleergen = set()
    for a_data in data:
        prefix_len = len('contains ')
        allergens = re.split(r'[,\s]\s*', a_data[1][prefix_len:])
        aleergen.update(allergens)
    # create and return data structure
    return data, aleergen


def main(input_f_name):
    '''The main function'''
    ingr_all, allrgens = parse_input(input_f_name)
    common_ingr = list()
    for alrgn in allrgens:
        algr_ingr = set()
        for ingr in ingr_all:
            if ingr[1].find(alrgn) != -1:
                algr_ingr.update(ingr[0].split())
        common_ingr.append(algr_ingr)

    non_alrgn = set.union(*common_ingr) - set.intersection(*common_ingr)
    print(non_alrgn)


if __name__ == '__main__':
    main(sys.argv[1])
