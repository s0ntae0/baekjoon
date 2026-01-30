import sys

input = sys.stdin.readline
N = int(input())
N_list = sorted(map(int,input().split()))

M = int(input())
M_list = map(int, input().split())

for m in M_list:
    left = 0
    right = len(N_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == m:
            print(1)
            break
        elif N_list[mid] < m:
            left = mid + 1
        else:
            right = mid- 1
    if N_list[mid] != m:
        print(0)