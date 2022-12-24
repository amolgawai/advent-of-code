"""Day 25 solution"""


def get_loop_size(pub_key):
    """Gets the secret loop size for generating the public key
    Keyword Arguments:
    pub_key -- public key for which loop size is required
    """
    subj_val = 7
    value = 1
    loop_var = 0
    while value != pub_key:
        loop_var += 1
        value = value * subj_val % 20201227

    return loop_var


def tranform_subj(subj_val, loop_var):
    """Tranforms the subject value by running a loop of loop_var
    Keyword Arguments:
    subj_val -- the subject value
    loop_var -- number of loops
    """
    value = 1
    for __ in range(loop_var):
        value = value * subj_val % 20201227

    return value


def main():
    """The main function"""
    # card_pub_key = 5764801
    # door_pub_key = 17807724
    card_pub_key = 19241437
    door_pub_key = 17346587
    card_loop = get_loop_size(card_pub_key)
    door_loop = get_loop_size(door_pub_key)
    encryption_key_1 = tranform_subj(card_pub_key, door_loop)
    encryption_key_2 = tranform_subj(door_pub_key, card_loop)
    assert encryption_key_1 == encryption_key_2
    print(card_loop, door_loop, encryption_key_1)


if __name__ == '__main__':
    main()
