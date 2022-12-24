"""Day 15 solution"""
from collections import defaultdict


def get_2020th_num(num_lst):
    """Gets the 2020th number spoken
    Keyword Arguments:
    num_lst -- initial number list
    """
    num_turn_dict = defaultdict(int)
    num_last = 0
    num_spoken = set()
    for turn in range(1, 11):
        if turn <= len(num_lst):
            num_last = num_lst[turn - 1]
            num_spoken.add(num_last)
        elif num_last in num_spoken:
            num_last = turn - 1 - num_turn_dict[num_last]
        else:
            num_spoken.add(num_last)
            num_last = num_lst[0]

        num_turn_dict[num_last] = turn

    print(num_spoken)
    print(num_turn_dict)
    return num_last


def main():
    """The main function"""
    numbers_t1 = [0, 3, 6]
    print(get_2020th_num(numbers_t1))


if __name__ == '__main__':
    main()
