# 4n^2 - 6n + 6
# n=5

tellen = [x for x in range(3, 1002, 2)]
total = []
for n in tellen:
    total.append((4 * (n**2) - (6 * n) + 6))

print(sum(total) + 1)