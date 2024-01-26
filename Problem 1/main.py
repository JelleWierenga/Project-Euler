temp = []
loop = 1001
for i in range(1, loop):
    calc = 5*i
    if calc < (loop - 1):
        temp.append(calc)

for j in range(1, loop):
    calc1 = 3*j
    if calc1 < (loop - 1):
        if calc1 not in temp:
            temp.append(calc1)

print(temp)
print(sum(temp))
