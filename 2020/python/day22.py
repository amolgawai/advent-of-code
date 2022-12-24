'''Day 22 solution'''
import sys
from collections import deque
import itertools


def parse_input(input_f_name):
    '''parses input from the given file name and returns data'''
    with open(input_f_name) as input_f:
        pl_1, pl_2 = input_f.read().split('\n\n')

    # create and return data structure
    pl1_name, *pl1_cards = pl_1.split('\n')
    pl2_name, *pl2_cards = pl_2.split('\n')
    return (pl1_name, deque(int(card.strip()) for card in pl1_cards if card)),\
        (pl2_name, deque(int(card.strip()) for card in pl2_cards if card))


def play_game(cards_1, cards_2, part2=False):
    """ Play the cards game
    Keyword Arguments:
    cards_1 -- first player cards
    cards_2 -- second player cards
    """

    crds_prev_1_lst = list()
    crds_prev_2_lst = list()
    while cards_1 and cards_2:
        crds_prev_1_lst.append(cards_1.copy())
        crds_prev_2_lst.append(cards_2.copy())
        c_1 = cards_1.popleft()
        c_2 = cards_2.popleft()
        if part2 and c_1 <= len(cards_1) and c_2 <= len(cards_2):
            wnr, __ = play_game(deque(itertools.islice(cards_1, c_1)),
                                deque(itertools.islice(cards_2, c_2)))
        else:
            wnr = 1 if c_1 > c_2 else 2

        if wnr == 1:
            cards_1.extend([c_1, c_2])
        else:
            cards_2.extend([c_2, c_1])

        if (cards_1 in crds_prev_1_lst) and (cards_2 in crds_prev_2_lst):
            # cards_2 = None
            # break
            return(1, list(cards_1))

    if cards_1:
        winner = list(cards_1)
        winner_num = 1
    else:
        winner = list(cards_2)
        winner_num = 2

    return(winner_num, winner)


def score(card_lst):
    """Calculates the score from cards
    Keyword Arguments:
    card_lst -- list of cards
    """

    winner_sum = 0
    mult = 1
    for value in reversed(card_lst):
        winner_sum += value * mult
        mult += 1

    return winner_sum


def main(input_f_name):
    '''The main function'''
    plyr_1, plyr_2 = parse_input(input_f_name)
    win_plyr, win_cards = play_game(plyr_1[1].copy(), plyr_2[1].copy())
    print(win_plyr, score(win_cards))

    win_plyr, win_cards = play_game(plyr_1[1].copy(), plyr_2[1].copy(), True)
    print(win_plyr, score(win_cards))


if __name__ == '__main__':
    main(sys.argv[1])
