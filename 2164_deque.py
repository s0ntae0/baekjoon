import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
card_list = deque(range(1,N+1))

while(len(card_list) > 1):
    card_list.popleft()
    card_list.append(card_list.popleft())
    
print(card_list[0])