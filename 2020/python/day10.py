"""Day 10 solution"""
import sys
from collections import Counter
from functools import lru_cache
import numpy as np


def part2_recurse(lst, num=0):
    """Recursive function for part 2,
    non memoized, takes a loooong time
    """
    return (num == len(lst) - 1) + sum(
        part2_recurse(lst, j) for j in range(num + 1, len(lst))
        if lst[num] + 3 >= lst[j]
    )


# for memoization, param must be hashable, hence tuple
@lru_cache(maxsize=None)
def part2_recurse_memoizd(tpl, num=0):
    """Memoized recursive function for part 2"""
    return (num == len(tpl) - 1) + sum(
        part2_recurse_memoizd(tpl, j) for j in range(num + 1, len(tpl))
        if tpl[num] + 3 >= tpl[j]
    )


def main(input_f_name):
    """ The main function"""
    with open(input_f_name) as input_f:
        adapter_lst = np.loadtxt(input_f, dtype=int)
    adapter_sortd = np.sort(np.insert(adapter_lst, 0, 0))
    # adapter_sortd = np.append(adapter_sortd, adapter_sortd[-1] + 3)
    diff_ar = np.diff(adapter_sortd)
    count_dict = Counter(diff_ar)
    print(diff_ar)
    print(count_dict)
    print(f"Thress - {count_dict[3]}, Ones - {count_dict[1]}")
    # print(part2_recurse(adapter_sortd))
    print(part2_recurse_memoizd(tuple(adapter_sortd)))


if __name__ == '__main__':
    main(sys.argv[1])
