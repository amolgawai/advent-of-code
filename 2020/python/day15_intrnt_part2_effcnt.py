"""day 15 efficient solution
source - https://github.com/Bruception/advent-of-code-2020/blob/master/day15/part2.py
"""
import sys

maxTurn = 30000000
line = [
    int(n) for n in open(f"{sys.path[0]}/input_day15.txt", "r").readline().split(",")
]
turnMap = [-1] * (maxTurn + 1)
for i, num in enumerate(line):
    turnMap[num] = i + 1
turn = len(line)
lastNum, nextNum = line[-1], 0
while turn < maxTurn:
    curr = turnMap[lastNum]
    turnMap[lastNum] = turn
    lastNum = 0 if curr == -1 else turn - curr
    turn += 1
print(lastNum)
