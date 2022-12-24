"""Day 12 concise soln fond on reddit"""
import sys

WIND_DIRS = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}


def navigate(instrs, waypoint):
    """Navigate according to the instructions, waypoint is optional"""
    xcord = ycord = 0
    dxcord, dycord = (10, 1) if waypoint else WIND_DIRS['E']

    for inst, param in instrs:
        if inst == 'L':
            for __ in range(param // 90):
                dxcord, dycord = -dycord, dxcord
        elif inst == 'R':
            for __ in range(param // 90):
                dxcord, dycord = dycord, -dxcord
        elif inst == 'F':
            xcord += dxcord * param
            ycord += dycord * param
        else:
            wdxcord, wdycord = WIND_DIRS[inst]
            if waypoint:
                dxcord += wdxcord * param
                dycord += wdycord * param
            else:
                xcord += wdxcord * param
                ycord += wdycord * param

    return abs(xcord) + abs(ycord)


def main(input_f_name):
    """The man function"""
    with open(input_f_name) as input_f:
        instructions = [(line[0], int(line[1:])) for
                        line in input_f.readlines()]
    print(navigate(instructions, False))
    print(navigate(instructions, True))


if __name__ == '__main__':
    main(sys.argv[1])
