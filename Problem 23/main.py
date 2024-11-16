abundant = []
for i in range(1, 28123):
    temp = []
    for j in range(1, i):
        if i//j * j == i:
            temp.append(j)
    if sum(temp) > i:
        abundant.append(i)



som = set()
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        # print(abundant[i] + abundant[j])
        som.add(abundant[i] + abundant[j])

klaar = sum([x for x in range(1, 28123) if x not in som])
print(klaar)