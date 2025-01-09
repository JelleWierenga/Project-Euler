import itertools

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Total = 0
for number in itertools.permutations(list):
    if number[0] == 0:
        continue

    d2d3d4 = int(''.join(map(str, number[1:4])))
    d3d4d5 = int(''.join(map(str, number[2:5])))
    d4d5d6 = int(''.join(map(str, number[3:6])))
    d5d6d7 = int(''.join(map(str, number[4:7])))
    d6d7d8 = int(''.join(map(str, number[5:8])))
    d7d8d9 = int(''.join(map(str, number[6:9])))
    d8d9d10 = int(''.join(map(str, number[7:10])))

    if (d2d3d4 % 2 == 0 and d3d4d5 % 3 == 0 and d4d5d6 % 5 == 0 and d5d6d7 % 7 == 0 and d6d7d8 % 11 == 0 and d7d8d9 % 13 == 0 and d8d9d10 % 17 == 0):
        completeNumber = int(''.join(map(str, number)))
        Total += completeNumber
        print(f"Geldig getal: {completeNumber}")

print(f"Totaal: {Total}")