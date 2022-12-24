"""Day 4 puzzle solution"""


def is_pass_valid_allchck(pass_str: str) -> bool:
    """ Performs all validity checks on passport

    Parameters
    ----------
    pass_str: str : the passport string


    Returns
    -------
    boolean : Tre if valid, else False

    """

    eye_clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pass_dict = dict(x.split(":") for x in pass_str.split())
    byr = pass_dict['byr']
    iyr = pass_dict['iyr']
    eyr = pass_dict['eyr']
    hcl = pass_dict['hcl']
    pass_id = pass_dict['pid']
    ht_valid = False
    unit_hgt = pass_dict['hgt'][-2:]
    if unit_hgt == 'cm':
        if 150 <= int(pass_dict['hgt'][:-2]) <= 193:
            ht_valid = True
    elif unit_hgt == 'in':
        if 59 <= int(pass_dict['hgt'][:-2]) <= 76:
            ht_valid = True
    else:
        pass
    return ((byr.isnumeric() and int(byr) in range(1920, 2002 + 1)) and
            (iyr.isnumeric() and int(iyr) in range(2010, 2020 + 1)) and
            (eyr.isnumeric() and int(eyr) in range(2020, 2030 + 1)) and
            (pass_dict['ecl'] in eye_clrs) and
            (len(pass_id) == 9 and pass_id.isnumeric()) and
            (len(hcl) == 7 and hcl[0] == '#' and hcl[1:].isalnum()) and
            ht_valid)


def get_valid_pass(check_all: bool, pass_data: list) -> int:
    """ Gets valid passport numbers

    Parameters
    ----------
    check_all: bool : wheather to check all values

    pass_data: list : list of passport data


    Returns
    -------
    int : number of valid passports

    """

    valid_pass_num = 0
    valid_data = ['byr:', 'iyr:', 'eyr:', 'hgt:',
                  'hcl:', 'ecl:', 'pid:', 'cid']
    for pass_info in pass_data:
        res = [ele for ele in valid_data if ele in pass_info]
        if len(res) > 6:
            if 'cid' in res and len(res) == 7:
                continue

            if check_all:
                if is_pass_valid_allchck(pass_info):
                    valid_pass_num += 1
            else:
                valid_pass_num += 1
    return valid_pass_num


def main():
    "The main function"
    with open('input_day4.txt') as data_f:
        pass_data_lst = data_f.read().split('\n\n')
    print("Puzzle 1 - ", get_valid_pass(False, pass_data_lst))
    print("Puzzle 2 - ", get_valid_pass(True, pass_data_lst))


if __name__ == '__main__':
    main()
