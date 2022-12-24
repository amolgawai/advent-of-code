""" The day 3 puzzle
"""


def trees_on_slope(right: int, down: int, the_map: list) -> int:
    """

    Parameters
    ----------
    right: int : the step to right of the slope

    down :int : the step down the slope


    Returns
    -------
    out : number o trees encountered

    """
    counter = 0
    trees = 0

    for x in range(down, len(the_map), down):
        counter += right
        the_line = the_map[x]
        if counter + 1 > len(the_line):
            the_line = the_line * (counter//len(the_line) + 1)
        if the_line[counter] == '#':
            trees += 1
    return trees


def main():
    """ The main function """
    with open('input_day3.txt') as in_file:
        the_map_input = in_file.read().splitlines()
    tr_1 = trees_on_slope(1, 1, the_map_input)
    tr_2 = trees_on_slope(3, 1, the_map_input)
    tr_3 = trees_on_slope(5, 1, the_map_input)
    tr_4 = trees_on_slope(7, 1, the_map_input)
    tr_5 = trees_on_slope(1, 2, the_map_input)
    print(tr_1, tr_2, tr_3, tr_4, tr_5)
    print(tr_1 * tr_2 * tr_3 * tr_4 * tr_5)


if __name__ == '__main__':
    main()
