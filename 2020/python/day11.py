"""Day 11 Solution"""
import sys


def add_adjacent_row(clmn, row):
    "Adds adjacent seats in a row"

    adj_seats_row = ''
    if clmn == 0:
        adj_seats_row += row[1]
    elif clmn == len(row) - 1:
        adj_seats_row += row[clmn - 1]
    else:
        adj_seats_row += row[clmn - 1]
        adj_seats_row += row[clmn + 1]

    return adj_seats_row


def get_adjacent_seats(row_num, clmn_num, seats):
    """Gets a list of adjacent seats given the seat colmn and row number"""
    seat_row = seats[row_num]
    row_above = ''
    if row_num != 0:
        row_above = seats[row_num - 1]
    row_below = ''
    if row_num < (len(seats) - 1):
        row_below = seats[row_num + 1]
    rows = [row_above,  row_below]
    ad_seats = add_adjacent_row(clmn_num, seat_row)
    for row in rows:
        if row == '':
            continue
        ad_seats += row[clmn_num]
        ad_seats += add_adjacent_row(clmn_num, row)
    return ad_seats


def get_new_arangmnt(orig_aragmnt):
    """ Gets a new seat arrangement """

    data_new = []
    for row, line in enumerate(orig_aragmnt):
        row_new = ''
        for clmn, seat in enumerate(line):
            adjcnt = get_adjacent_seats(row, clmn, orig_aragmnt)
            if (seat == 'L') and (adjcnt.count('#') == 0):
                seat = '#'
            elif (seat == '#') and (adjcnt.count("#") > 3):
                seat = 'L'
            row_new += seat
        data_new.append(row_new)
    return data_new


def main(input_f_name):
    """The main function"""
    with open(input_f_name) as input_f:
        # data = [[ltr for ltr in line.strip()] for line in input_f.readlines()]
        data = [line.strip() for line in input_f.readlines()]

    print("Orig data")
    for a_row in data:
        print(a_row)

    rounds = 0
    done = False
    while not done:
        rounds += 1
        data_r = get_new_arangmnt(data)
        for new_r in data_r:
            print(new_r)

        if data_r == data:
            print("Done")
            done = True
        else:
            print("Not done")
            data = data_r

    occupied = 0
    for st_rw in data:
        occupied += st_rw.count('#')

    print(rounds, occupied)


if __name__ == '__main__':
    main(sys.argv[1])
