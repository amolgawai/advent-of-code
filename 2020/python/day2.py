"""Day 2 puzzle solution
"""
import pandas as pd


def is_pwd_valid_pos(row):
    " Finds if the password is valid given the dataframe row for puzzle 2"
    mnmx = [int(x)-1 for x in row[0].split('-')]
    pwd_str = row[2]
    pwd_char= row[1][0]
    if len(pwd_str) < mnmx[1]:
        return False
    pos = [pos for pos, char in enumerate(pwd_str) if char == pwd_char]
    res = [x for x in mnmx if x in pos]
    return len(res) == 1


def is_pwd_valid(row):
    " Finds if the password is valid given the dataframe row for puzzle 1"
    mnmx = [int(x) for x in row[0].split('-')]
    return mnmx[0] <= row[2].count(row[1][0]) <= mnmx[1]


def main():
    "The main function"
    pwd_df = pd.read_csv("input_day2.txt", delim_whitespace=True, header=None)
    # puzzle 1
    result = pwd_df.apply(is_pwd_valid, axis=1)
    print("puzzle 1 - ", result.value_counts())
    # puzzle 2
    result1 = pwd_df.apply(is_pwd_valid_pos, axis=1)
    print("puzzle 2 - ", result1.value_counts())


if __name__ == '__main__':
    main()
