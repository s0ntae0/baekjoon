N = int(input())
dot_list = []
for i in range(N):
    dot_list.append(tuple(map(int, input().split())))
dot_list.sort(key= lambda x : (x[1],x[0]))


for i in range(N):
    print(dot_list[i][0], dot_list[i][1])