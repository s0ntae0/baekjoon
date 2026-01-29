N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

k = 1

for i in lst:
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            k += 1
    print(k, end=' ')
    k = 1
