from collections import defaultdict
import sys
N = int(input())
lst = defaultdict(list)
input = sys.stdin.readline
for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst[age].append(name)

lst = dict(lst)
age_lst = list(lst.keys())
age_lst.sort()

for i in age_lst:
    for j in lst[i]:
        print(i,j, sep=" ")