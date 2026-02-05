from collections import deque
import sys, math

input = sys.stdin.readline
n = int(input())
if n ==0:
    print(0)
else:
    level = []
    for i in range(n):
        level.append(int(input()))

    level.sort()
    level_sorted = deque(level)
    a = math.floor(n*15/100 + 0.5)
    for i in range(a):
        level_sorted.pop()
        level_sorted.popleft()

    print(math.floor(sum(level_sorted)/len(level_sorted)+0.5))
