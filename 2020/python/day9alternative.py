numbers = (int(n.strip()) for n in open('input_day9.txt', 'r').readlines())
seen = set()
seen_in_order = list()
preamble = 25

for i in range(preamble):
    number = next(numbers)
    seen.add(number)
    seen_in_order.append(number)

while True:
    number = next(numbers)
    for n in seen:
        if number - n in seen:
            to_remove = seen_in_order[-25]
            seen.remove(to_remove)
            seen.add(number)
            seen_in_order.append(number)
            break
    else:
        sol1 = number
        print(sol1)
        break


def recursive_variant(seen_in_order, score, min_index, max_index, target):
    if score == target:
        return min(seen_in_order[min_index:max_index]) + \
               max(seen_in_order[min_index:max_index])
    if score > target:
        return recursive_variant(seen_in_order,
                                 score - seen_in_order[min_index],
                                 min_index+1,
                                 max_index,
                                 target)
    return recursive_variant(seen_in_order,
                             score + seen_in_order[max_index+1],
                             min_index,
                             max_index+1,
                             target)


print(recursive_variant(seen_in_order, seen_in_order[0], 0, 0, sol1))
