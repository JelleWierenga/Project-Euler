largest_factor = 2
num = 600851475143

while num % 2 == 0:
    largest_factor = 2
    num = num // 2

for i in range(3, int(num**0.5) + 1, 2):
    while num % i == 0:
        largest_factor = i
        num = num // i

if num > 2:
    largest_factor = num

print(largest_factor)
