sum = 1
for i in range(1, 101):
    print(i)
    sum = sum * i


sum = str(sum)
total = 0
for i in sum:
    total += int(i)
print(total)