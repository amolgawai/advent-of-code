"""Day 6 puzzle solution"""
from collections import defaultdict


class CICounter(defaultdict):
    def __getitem__(self, k):
        return super().__getitem__(k.lower())

    def __setitem__(self, k, v):
        super().__setitem__(k.lower(), v)


def count_chars(str_cnt):
    """Count the characters in a string """
    chars = CICounter(int)
    for char in str_cnt:
        if char == '\n':
            continue
        chars[char] += 1
    return chars


def puzzle_1(lst_ans):
    """ Answers to puzzle 1"""
    ans = [count_chars(ques) for ques in lst_ans]
    return sum(map(len, ans))


def puzzle_2(lst_ans):
    """Answer to puzzle 2 """
    total = 0
    # count answers if everyone has said yes to that answer
    for group_ans in lst_ans:
        ans_lines = group_ans.splitlines()
        char_dict = count_chars(group_ans)
        for __, count in char_dict.items():
            if count == len(ans_lines):
                total += 1
    return total


def main():
    "The main function"
    with open('input_day6.txt') as data_f:
        ques_data_lst = data_f.read().split('\n\n')
    print(puzzle_1(ques_data_lst))
    print(puzzle_2(ques_data_lst))


if __name__ == '__main__':
    main()
