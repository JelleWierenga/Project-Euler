lijst = []

for num in range(2, 2000000):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        lijst.append(num)
        print(num)

print(sum(lijst))


# Output: 142913828922
# TOOK ME FLIPPING AGES TO RUN THIS CODE