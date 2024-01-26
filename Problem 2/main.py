num1 = 0
num2 = 1
fib = []
for i in range(100000):
    sum1 = num1 + num2
    num1 = num2
    num2 = sum1
    if sum1 < 4000000:
        if (sum1 % 2) == 0:
            fib.append(sum1)
        else:
            continue
    else:
        continue

print(sum(fib))
