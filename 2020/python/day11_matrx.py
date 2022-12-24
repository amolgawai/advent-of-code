"""Day 11 solution with matrices"""
import sys
import pprint


def check_ele_and_add(ele, lst):
    """ Checks if element is not a '.' and then adds it to the list"""
    if ele != '.':
        lst.append(ele)
        return True
    return False


def check_bounds(row_indx, clmn_indx, r_len, c_len):

    if (row_indx < 0 or row_indx >= r_len) or (clmn_indx < 0 or clmn_indx >= c_len):
        return False
    return True


def get_adjacent_eles_alt1(row, clm, row_len, clmn_len, matrix):
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    adjcnts = []
    for dirct in dirs:
        advance_check = True
        dr, dc = dirct
        cell_r = row
        cell_c = clm
        while advance_check:
            cell_r += dr
            cell_c += dc
            if not check_bounds(cell_r, cell_c, row_len, clmn_len):
                advance_check = False
            else:
                advance_check = not check_ele_and_add(matrix[cell_r][cell_c], adjcnts)

    # print(adjcnts)
    return adjcnts


def get_adjacent_eles(row, clm, row_len, clmn_len, matrix):
    """Gets adjacent elements of a column """

    adjcnt_eles = []
    # traverse left
    for clmn_l in range(clm - 1, -1, -1):
        if check_ele_and_add(matrix[row][clmn_l], adjcnt_eles):
            break

    # traverse right
    for clmn_l in range(clm + 1, clmn_len):
        if check_ele_and_add(matrix[row][clmn_l], adjcnt_eles):
            break

    # traverse up
    for up_idx in range(row-1, -1, -1):
        if check_ele_and_add(matrix[up_idx][clm], adjcnt_eles):
            break

    # traverse down
    for up_idx in range(row+1, row_len):
        if check_ele_and_add(matrix[up_idx][clm], adjcnt_eles):
            break

    # traverse up-left
    clm_indx = clm - 1
    for up_idx in range(row-1, -1, -1):
        if clm_indx < 0:
            break
        if check_ele_and_add(matrix[up_idx][clm_indx], adjcnt_eles):
            break
        clm_indx -= 1

    # traverse right-up
    clm_indx = clm + 1
    for up_idx in range(row-1, -1, -1):
        if clm_indx >= clmn_len:
            break
        if check_ele_and_add(matrix[up_idx][clm_indx], adjcnt_eles):
            break
        clm_indx += 1

    # traverse down-left
    clm_indx = clm - 1
    for up_idx in range(row+1, row_len):
        if clm_indx < 0:
            break
        if check_ele_and_add(matrix[up_idx][clm_indx], adjcnt_eles):
            break
        clm_indx -= 1

    # traverse roght-down
    clm_indx = clm + 1
    for up_idx in range(row+1, row_len):
        if clm_indx >= clmn_len:
            break
        if check_ele_and_add(matrix[up_idx][clm_indx], adjcnt_eles):
            break
        clm_indx += 1

    return adjcnt_eles


def print_data(data):
    for a_row in data:
        for ele in a_row:
            print(ele, end='')
            # str_row.join(ele)
        print('\n', end='')

    print('\n')


def get_new_arangmnt(data):
    """Gets a new seat arrangement as per rules"""
    row_len = len(data)
    clmn_len = len(data[0])
    new_data = []
    for row_num in range(len(data)):
        new_row = []
        for clmn_num in range(len(data[0])):
            data_ele = data[row_num][clmn_num]
            if data_ele != '.':
                adjcnt = get_adjacent_eles_alt1(row_num,
                                                clmn_num,
                                                row_len,
                                                clmn_len,
                                                data)
                if (data_ele == 'L') and (adjcnt.count('#') == 0):
                    data_ele = '#'
                elif (data_ele == '#') and (adjcnt.count("#") > 4):
                    data_ele = 'L'
            new_row.append(data_ele)
        new_data.append(new_row)

    return new_data


def main(input_f_name):
    """The main function"""

    with open(input_f_name) as input_f:
        data = [[ltr for ltr in line.strip()] for line in input_f.readlines()]

    # pprint.pprint(data)

    rounds = 0
    done = False
    while not done:
        rounds += 1
        data_r = get_new_arangmnt(data)
        # print_data(data_r)

        if data_r == data:
            done = True
        else:
            data = data_r

    occupied = 0
    for st_rw in data:
        occupied += st_rw.count('#')
    print(occupied)


if __name__ == '__main__':
    main(sys.argv[1])
