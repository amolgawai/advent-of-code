"""Simple solution to day 6"""

with open('input_day6.txt') as input_f:
    ans_lines = [a.strip().split('\n') for a in input_f.read().split('\n\n')]

# part 1
# create list of sets of answers per group
ans_set = [set(''.join(a)) for a in ans_lines]
print(sum(map(len, ans_set)))

# part 2
# create list for each group containing list of sets for each answer
ans_group_set = [[set(a) for a in sublist] for sublist in ans_lines]
# find common answers for each group
ans_set_ints = [set.intersection(*group) for group in ans_group_set]
print(sum(map(len, ans_set_ints)))
