"""Day 9 solution"""
import numpy as np
from day1 import find_nums_sum


def find_cont_sub_lst_with_sum(num_list, tot):
    """Finds a contgeous sub list with sum == tot"""

    found_sum = False
    sub_lst = None
    for indx1 in range(len(num_list)):
        if found_sum:
            break
        sub_sub_list = num_list[indx1:]
        max_sum = sum(sub_sub_list)
        if max_sum == tot:
            sub_lst = sub_sub_list
            found_sum = True
            break
        for indx_cur in range(len(sub_sub_list)-1, 0, -1):
            max_sum -= sub_sub_list[indx_cur]
            if max_sum == tot:
                sub_lst = sub_sub_list[:indx_cur]
                found_sum = True
                break
    return sub_lst


def find_cont_sub_lst_with_sum_rec(num_list, init_sum, tot):
    """Finds a contgeous sub list with sum == tot
       returns empty list if not found
    Parameters
    ----------
    num_list: list from which sublist is requested

    init_sum: is the initial sum of all the elements

    tot: the target total


    Returns
    --------
    out: sulist if found else empty list
    """

    max_sum = init_sum
    if max_sum == tot:
        return num_list
    if max_sum < tot or len(num_list) == 1:
        return []
    for indx_cur in range(len(num_list)-1, 0, -1):
        max_sum -= num_list[indx_cur]
        if max_sum == tot:
            return num_list[:indx_cur]
        if max_sum < tot:
            break
    return find_cont_sub_lst_with_sum_rec(num_list[1:],
                                          init_sum - num_list[0],
                                          tot)


def main(input_f_name, preamble=25):
    "The main function"
    num_list = np.loadtxt(input_f_name)
    for indx, num in enumerate(num_list[preamble:]):
        sub_list = num_list[indx:indx+preamble]
        if not find_nums_sum(sub_list, num, 2):
            invalid_num = num
            print(f"Puzzle 1 number - {num}")
            break
    sum_lst = find_cont_sub_lst_with_sum_rec(num_list,
                                             sum(num_list),
                                             invalid_num)
    if sum_lst.any():
        max_num = max(sum_lst)
        min_num = min(sum_lst)
        print(f"Puzzle 2 - {max_num} + {min_num} = {max_num + min_num}")


if __name__ == '__main__':
    # main("input_test_day9.txt", 5)
    main("input_day9.txt")
