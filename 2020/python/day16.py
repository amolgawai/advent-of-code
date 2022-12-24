"""Day 16 solution"""
import sys
import re
from collections import defaultdict


def get_rule_ranges(rules):
    """Gets a collection of rule ranges from a rule string
    Keyword Arguments:
    rules -- a string containing rules
    """
    rules_dict = defaultdict(list)
    for a_line in rules.splitlines():
        rule_name = a_line.split(':')[0]
        rule_values = [[int(val) for val in pair.split('-')]
                       for pair in re.findall(r'(\d+-\d+)', a_line)]
        rules_dict[rule_name] = rule_values
    return rules_dict


def main(input_f_name):
    """The main function of the script"""
    with open(input_f_name) as input_f:
        data = input_f.read().split('\n\n')

    rule_dict = get_rule_ranges(data[0])
    ranges = list()
    for values in rule_dict.values():
        ranges += [value for value in values]
    my_ticket = [int(val) for val in data[1].split()[-1].split(',')]
    tickets = list()
    for a_line in data[2].splitlines()[1:]:
        tickets.append([int(val) for val in a_line.split(',')])

    invalid_sum = 0
    valid_tckts = list()
    for a_ticket in tickets:
        is_valid = True
        for a_value in a_ticket:
            if not any(a_value in range(a_range[0], a_range[1] + 1) for a_range in ranges):
                invalid_sum += a_value
                is_valid = False
                break
        if is_valid:
            valid_tckts.append(a_ticket)

    print(invalid_sum)
    order = list()
    for a_tckt in valid_tckts:
        tckt_rngs = list()
        for num in a_tckt:
            num_rng = list()
            for rng in ranges:
                if rng[0] <= num <= rng[1]:
                    num_rng.append(rng)
            tckt_rngs.append(num_rng)
        order.append(tckt_rngs)

    for a_vld_rng in order:
        print(a_vld_rng)
    # print(valid_tckts)


if __name__ == '__main__':
    main(sys.argv[1])
