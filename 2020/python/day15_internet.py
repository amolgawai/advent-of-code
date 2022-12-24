from collections import defaultdict, deque


def play(numbers, end_turn):
    memory = defaultdict(lambda: deque([], maxlen=2))
    for turn, n in enumerate(numbers, start=1):
        memory[n].append(turn)
    last_num = n
    for turn in range(turn+1, end_turn+1):
        last_seen = memory[last_num]
        if len(last_seen) == 1:
            last_num = 0
        else:
            last_num = last_seen[1] - last_seen[0]
        memory[last_num].append(turn)
    print(f"Output for {numbers} on turn {turn} = {last_num}.",
          f"The memory has length {len(memory)}.")
    return last_num


nums = [20, 9, 11, 0, 1, 2]
print(play(nums, 2020))
print(play(nums, 30000000))
