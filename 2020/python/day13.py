"""Day 13 solution"""
import sys
from collections import defaultdict


def main(input_f_name):
    """The main function"""
    with open(input_f_name) as input_f:
        data = input_f.readlines()

    t_stamp = int(data[0])
    bus_ids = [int(b_id) for b_id in data[1].split(',') if b_id != 'x']
    bid_t_dict = defaultdict()
    for bus_id in bus_ids:
        next_b_time = (t_stamp//bus_id)*bus_id
        print(bus_id, next_b_time)
        found = False
        while not found:
            next_b_time += bus_id
            if next_b_time >= t_stamp:
                found = True
                bid_t_dict[bus_id] = next_b_time - t_stamp
    # print(t_stamp, bus_ids)
    print(bid_t_dict)
    min_diff = min(bid_t_dict.values())
    min_id = list(bid_t_dict.keys())[list(bid_t_dict.values()).index(min_diff)]
    print(min_diff * min_id)


if __name__ == '__main__':
    main(sys.argv[1])
