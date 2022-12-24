'''Day 19 solution'''
import sys
import re
from collections import defaultdict


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        rules, msgs = input_f.read().split('\n\n')

    # create and return data structure
    rules_dict = defaultdict(str)
    base_rules_dict = defaultdict(str)
    for rule in rules.split('\n'):
        r_num, r_value = rule.split(':')
        # rules_dict[r_num] = r_value.strip().strip(r'"')
        if not re.search(r'\d+', r_value):
            base_rules_dict[r_num] = r_value.strip().strip(r'"')
        else:
            rules_dict[r_num] = r_value

    for a_rule_num, a_rule_str in rules_dict.items():
        print(a_rule_num, a_rule_str)

    return (rules_dict, msgs.split('\n'))


def main(input_f_name):
    '''The main function'''
    rule_lst, msg_lst = parse_input(input_f_name)
    print(rule_lst, msg_lst)


if __name__ == '__main__':
    main(sys.argv[1])
