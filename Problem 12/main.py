def factors(n):
    lijst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lijst.append(i)
    return lijst

print(factors(28))

num = 1
while True:
    factors(num)
    num += 1
    if len(factors(num)) == 500:
        print(num)
        print(factors(num))
        break