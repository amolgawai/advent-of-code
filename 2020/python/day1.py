"""Day 1 puzzle solution
Puzzle 1 - Find two numbers in a list with sum 2020, return their product
Puzzle 2 - Find three numbers whose sum is 220, return their product
"""
from collections import Counter
import itertools as itrt
import numpy as np


def puzzle1(array_in, tot):
    """
    Finds the two numbers with sum == tot and returns their product
    """
    ar1 = np.array(array_in)
    ar2 = abs((ar1 - tot) + ar1)
    print(ar2)
    indices = np.where(ar2 == [item for item, count in Counter(ar2).items() if count > 1])
    values = []
    for indx in indices:
        values.append(ar1[indx])
    # print(len(values), values, sum(values))
    # assert len(values) == 2
    # assert sum(values) == 2020
    # print(np.prod(values))
    return np.prod(values)


def puzzle2(array_in, tot):
    """ Finds 3 numbers whose sum is tot and returns their product

    Parameters
    ----------
    array_in : array with numbers

    tot : total to be calculated


    Returns
    -------
    out : the product of three numbers

    """
    for a, b, c in itrt.combinations(array_in, 3):
        if a + b + c == tot:
            # print(a, b, c, a*b*c)
            return a*b*c
    return None


def find_nums_sum(array_in, tot, nums):
    """ Finds the numbers with total == tot

    Parameters
    ----------
    array_in : array of the numbers

    tot : the total of the numbers

    nums : how many numbers


    Returns
    -------
    tuple : the tuple of fund numbers

    """
    for lst in itrt.combinations(array_in, nums):
        if sum(lst) == tot:
            return lst
    return None


def main():
    """ The man function"""
    # x = [1000, 2000, 20, 50]
    x = np.loadtxt('input.txt')
    tot = 2020.0
    # print(find_nums_sum(x, tot, 2))
    # print(find_nums_sum(x, tot, 3))
    print("Two number product - ", np.prod(find_nums_sum(x, tot, 2)))
    print("Three number product - ", np.prod(find_nums_sum(x, tot, 3)))
    # print("two numbers product is " - puzzle1(x, tot))
    # print("three numbers product is " - puzzle2(x, tot))


if __name__ == '__main__':
    main()
