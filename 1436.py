N = int(input())

count = 0
end_nums = 666
while True:
    if '666' in str(end_nums):
        count +=1
        if count == N:
            print(end_nums)
            break
    end_nums += 1