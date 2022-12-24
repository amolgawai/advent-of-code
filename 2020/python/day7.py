"""Day 7 solution"""

test_input = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
              'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
              'bright white bags contain 1 shiny gold bag.',
              'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
              'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
              'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
              'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
              'faded blue bags contain no other bags.',
              'dotted black bags contain no other bags.']


def can_contain_gold_bag(bags_tpl_lst, bags_dict, base_bgs_lst):
    """returns true if the bag cn contain a shiny gold bag """
    bgs_lst = [bg_tpl[1] for bg_tpl in bags_tpl_lst]
    if 'shiny gold' in bgs_lst:
        return True
    for rec_bag in bgs_lst:
        if rec_bag in base_bgs_lst:
            continue

        if can_contain_gold_bag(bags_dict[rec_bag],
                                bags_dict,
                                base_bgs_lst):
            return True
    return False


def parse_bags(bags_str_lst):
    """ Parses the bags string and returns a tuple of bags, base_bags,
        shiny gold
    Keyword Arguments:
    bags_str_lst -- the bags string list
    """

    bags = [bag.split(' bags contain ') for bag in bags_str_lst]
    base_bags = [a_bag[0] for a_bag in bags if a_bag[1] == "no other bags."]
    shiny_gold = [g_bag for g_bag in bags if g_bag[0] == "shiny gold"]
    bags = [rd_bag for rd_bag in bags if rd_bag[0] not in base_bags]
    bags = [rd_bag for rd_bag in bags if rd_bag[0] != "shiny gold"]
    return(base_bags, shiny_gold, bags)


def get_gold_bag_clrs(input_str_lst):
    """ gets number of colors that can cotain gold bags
    Keyword Arguments:
    input_str_lst -- input list of bag rules
    """
    bse_bags, __, bgs = parse_bags(input_str_lst)
    the_bgs_dict = create_bag_dict_num(bgs)
    counter = 0
    for __, bgs_tpl in the_bgs_dict.items():
        if can_contain_gold_bag(bgs_tpl, the_bgs_dict, bse_bags):
            counter += 1
    return counter


def create_bag_dict_num(bags_lst):
    """ Creates a dictionary of bags
    Keyword Arguments:
    bags_lst -- the list of bags
    """
    bag_dict = dict()
    for bag in bags_lst:
        comp_bag_lst = list()
        comp_bags = bag[1].split(',')
        for comp_bag in comp_bags:
            num_bags_str, c_bag_str = comp_bag.strip().split(" ", 1)
            num_bags = int(num_bags_str)
            c_bag = c_bag_str.rsplit(" ", 1)[0]
            comp_bag_lst.append((num_bags, c_bag))
        bag_dict[bag[0]] = comp_bag_lst
    return bag_dict


def get_bg_tot(bags_tupl_lst, bags_dict, base_bgs_lst):
    """Get number of bags inside a bag"""
    bg_tot = 0
    for tpl in bags_tupl_lst:
        num, bg = tpl
        if bg in base_bgs_lst:
            bg_tot += num
        else:
            bg_tot += num + num * get_bg_tot(bags_dict[bg],
                                             bags_dict, base_bgs_lst)
    return bg_tot


def get_gold_bg_total(inpt_str):
    """gets total number of bags inside gold bag"""
    bse, gld, bgs = parse_bags(inpt_str)
    gld_bgs = create_bag_dict_num(gld)
    bags_dict = create_bag_dict_num(bgs)
    gld_name = gld[0][0]
    return get_bg_tot(gld_bgs[gld_name], bags_dict, bse)


def solve_puzzles(input_str):
    """Test with predetermined input"""
    print('Puzzle 1 - ')
    print(get_gold_bag_clrs(input_str))
    print('Puzzle 2 - ')
    print(get_gold_bg_total(input_str))


def main():
    """The main function"""
    # print(get_gold_bag_clrs(test_input))
    with open('input_day7.txt') as input_f:
        puzzle_1_lst = input_f.read().splitlines()
    solve_puzzles(puzzle_1_lst)


def test():
    """Test the puzzle solution"""
    solve_puzzles(test_input)


if __name__ == '__main__':
    main()
    # test()
