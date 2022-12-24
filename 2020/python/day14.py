"""Day 14 solution"""
import sys


def main(input_f_name):
    """The main function"""
    with open(input_f_name) as input_f:
        data = input_f.readlines()

    mask_str = data[0].strip()
    # values = [(mem.strip(), value.strip()) in val.split('=') for val in data[1:]]
    mem_val = list()
    for a_value in data:
        mem, value = a_value.split('=')
        mem_val.append((mem.strip(), value.strip()))
    # print(mask, mem_val)
    __, mask = mask_str.split('=')
    mask.strip()
    # mask = mask.replace('X', '0')
    mask_ones = []
    mask_zeros = []
    for pos, char in enumerate(mask):
        if char == '1':
            mask_ones.append(pos)
        elif char == '0':
            mask_zeros.append(pos)
    print(mask_ones, mask_zeros)
    print(f'mask   ->{mask}')
    for a_mem, a_val in mem_val[1:]:
        # a_val_b_str = f'{int(a_val):036b}'
        print(f'{a_mem} -> {int(a_val):036b}')


if __name__ == '__main__':
    main(sys.argv[1])
