
"""Day 11 solution with matrices"""
import sys


def get_valid_neighbours(row, clm, row_len, clmn_len, matrix):
    """ Gets valid neighbours for a matrix cell"""

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    adjcnts = []
    for diff_r, diff_c in dirs:
        advance_check = True
        cell_r = row
        cell_c = clm
        while advance_check:
            cell_r += diff_r
            cell_c += diff_c
            if not ( 0 <= cell_r < row_len and 0 <= cell_c < clmn_len):
                advance_check = False
            else:
                ele = matrix[cell_r][cell_c]
                if ele != '.':
                    adjcnts.append(ele)
                    advance_check = False

    return adjcnts


def get_new_arangmnt_if_changed(data):
    """Gets a new seat arrangement as per rules"""
    row_len = len(data)
    clmn_len = len(data[0])
    new_data = []
    is_change = False
    for row_num in range(len(data)):
        new_row = []
        for clmn_num in range(len(data[0])):
            data_ele = data[row_num][clmn_num]
            if data_ele != '.':
                adjcnt = get_valid_neighbours(row_num,
                                              clmn_num,
                                              row_len,
                                              clmn_len,
                                              data)
                if (data_ele == 'L') and (adjcnt.count('#') == 0):
                    data_ele = '#'
                    is_change = True
                elif (data_ele == '#') and (adjcnt.count("#") > 4):
                    data_ele = 'L'
                    is_change = True
            new_row.append(data_ele)
        new_data.append(new_row)

    return new_data if is_change else None


def main(input_f_name):
    """The main function"""

    with open(input_f_name) as input_f:
        data = [[ltr for ltr in line.strip()] for line in input_f.readlines()]

    rounds = 0
    done = False
    while not done:
        rounds += 1
        data_r = get_new_arangmnt_if_changed(data)

        if not data_r:
            done = True
        else:
            data = data_r

    occupied = 0
    for st_rw in data:
        occupied += st_rw.count('#')
    print(f'Occupied Seats = {occupied}')


if __name__ == '__main__':
    main(sys.argv[1])
