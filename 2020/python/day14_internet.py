import collections
import itertools
import re


def part_1(program):
    memory = collections.defaultdict(int)
    mask_to_0 = 0
    mask_to_1 = 0
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
            mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
            mask_to_0 = int("".join(m if m == "0" else "1" for m in mask), 2)
        else:
            address, value = (int(x) for x in re.findall(r"(\d+)", line))
            memory[address] = (value | mask_to_1) & mask_to_0
    return sum(memory.values())


def part_2(program):
    memory = collections.defaultdict(int)
    mask_to_1 = 0
    float_positions = []
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
            mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
            float_positions = [m.start() for m in re.finditer('X', mask)]
        else:
            address, value = (int(x) for x in re.findall(r"(\d+)", line))
            address = address | mask_to_1
            address = list(bin(address)[2:].zfill(36))
            for bits in itertools.product("01", repeat=len(float_positions)):
                for b, i in zip(bits, float_positions):
                    address[i] = b
                memory[int("".join(address), 2)] = value
    return sum(memory.values())


test_input_1 = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()
assert part_1(test_input_1) == 165

test_input_2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()
assert part_2(test_input_2) == 208

with open("input_day14.txt") as file:
    challenge_input = file.read().splitlines()
print(part_1(challenge_input))  # 4297467072083
print(part_2(challenge_input))  # 5030603328768
