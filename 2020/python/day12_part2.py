"""Day 12 solution"""
import sys
import re


REG_EX = re.compile("([a-zA-Z]+)([0-9]+)")


def main(input_f_name):
    """The main function"""
    with open(input_f_name) as input_f:
        instructions = [instr.strip() for instr in input_f.readlines()]
    instructions = [REG_EX.match(string).groups() for string in instructions]
    ship_manhatten = [0, 0]
    waypoint = [10, 1]
    ship_dir = "E"
    dirs = 'ESWN'
    rotation_indx = {0: 0, 0.25: 1, 0.50: 2, 0.75: 3}
    for instr, value in instructions:
        value = int(value)
        print(instr, value)
        if instr == 'F':
            move_by = waypoint * value
            if ship_dir == 'E':
                ship_manhatten[0] += move_by[0]
            elif ship_dir == 'W':
                ship_manhatten[0] -= move_by[0]
            elif ship_dir == 'S':
                ship_manhatten[1] -= move_by[1]
            else:
                ship_manhatten[1] += move_by[1]
        elif instr in 'RL':
            itrs = float(value) / 360.0
            itrs = itrs % 1
            indx = rotation_indx[itrs]
            if instr == 'L':
                indx = -indx
            dir_indx = dirs.index(ship_dir)
            new_dir_indx = dir_indx + indx
            if new_dir_indx > 3:
                new_dir_indx = new_dir_indx - 4
            ship_dir = dirs[new_dir_indx]
        else:
            if instr in 'EW':
                if instr == 'W':
                    waypoint[0] -= value
                else:
                    waypoint[0] += value
            else:
                if instr == 'S':
                    waypoint[1] -= value
                else:
                    waypoint[1] += value
        print(ship_dir, ship_manhatten)
    manhatten = abs(ship_manhatten[0]) + abs(ship_manhatten[1])
    print(f'Ships manhatten - {manhatten}, position - {ship_dir}, {ship_manhatten}')


if __name__ == '__main__':
    main(sys.argv[1])
