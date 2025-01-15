primes = []
for getal in range(2, 1000001):
    for i in range(2, int(getal**0.5) + 1):
        if getal % i == 0:
            break
    else:
        primes.append(getal)
primes_set = set(primes)

total = 0
for prime in primes:
    is_circular = True
    num_str = str(prime)
    for i in range(len(num_str)):
        rotated = int(num_str[i:] + num_str[:i])
        if rotated not in primes_set:
            is_circular = False
            break
    if is_circular:
        print(prime)
        total += 1

print(total)