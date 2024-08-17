length = 0
highest = 0
for i in range(1, 1000000):
    num = i
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        length += 1
    if length > highest:
        highest = length
        print(i, highest)
    length = 0


