values = []
for i in range(1, 1001):
    values.append(i**i)

print(str(sum(values))[-10:])