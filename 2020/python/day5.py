"""Day 5 puzzle solution"""


def binary_parition(lst: list, is_front: bool) -> list:
    """
    Partions the given list from front or back
    Parameters
    ----------
    lst: list : the list to be partiotioned

    is_front: bool : start from Front


    Returns
    -------
    out : The partitioned list

    """
    half_ln = int(len(lst)/2)
    if is_front:
        return lst[:half_ln]
    return lst[-half_ln:]


def find_seat_num(board_pass: str) -> tuple:
    """
    Finds the seat number given a boarding pass string
    Parameters
    ----------
    board_pass: str : The boarding pass string


    Returns
    -------
    out : the seat number tuple

    """

    r_num = board_pass[:7]
    c_num = board_pass[-3:]
    r_res = [*range(128)]  # rows
    c_res = [*range(8)]  # clmns
    for ltr_r in r_num:
        r_res = binary_parition(r_res, ltr_r == 'F')
    for ltr_c in c_num:
        c_res = binary_parition(c_res, ltr_c == 'L')
    return(r_res[0], c_res[0])


def get_seat_id(row_id: int, clmn_id: int) -> int:
    """
    Gets the seat id given row and column id
    """
    return (row_id * 8) + clmn_id


def get_test_input():
    """Gets the test input"""
    return ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']


def get_puzzle_input():
    """Gets the puzzle input by reading file"""
    with open('input_day5.txt') as in_file:
        the_map_input = in_file.read().splitlines()
    return the_map_input


def main():
    """The main function"""
    seat_ids = set()
    for brd_pass in get_puzzle_input():
        row_num, clmn_num = find_seat_num(brd_pass)
        seat_ids.add(get_seat_id(row_num, clmn_num))
    print(f" max seat id - {max(seat_ids)}, min seat id - {min(seat_ids)}")
    for seat_id in seat_ids:
        if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
            print(f"Missing boarding pass seat - {seat_id + 1}")


if __name__ == '__main__':
    main()
