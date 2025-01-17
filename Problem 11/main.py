import math

matrix = [
[8, 0o2, 22, 97, 38, 15, 00, 40, 00, 75, 0o4, 0o5, 0o7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 0o4, 56, 62, 00],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 0o3, 49, 13, 36, 65],
[52, 70, 95, 23, 0o4, 60, 11, 42, 69, 24, 68, 56, 0o1, 32, 56, 71, 37, 0o2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 0o3, 45, 0o2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 0o2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 0o5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 0o3, 80, 0o4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 0o5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 00, 48, 35, 71, 89, 0o7, 0o5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 0o5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 0o4, 89, 55, 40],
[0o4, 52, 8, 83, 97, 35, 99, 16, 0o7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 0o3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[0o4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 0o4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 0o1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 0o5, 54],
[0o1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 0o1, 89, 19, 67, 48]]

highest = 0
place = []

for i in range(20):
    for j in range(17):
        frst_four_numbers = matrix[i][j:j+4]
        som = math.prod(frst_four_numbers)
        print(som)
        print(frst_four_numbers)
        print("\n")
        if som > highest:
            highest = som
            place = frst_four_numbers


for i in range(17):
    for j in range(20):
        first_four_numbers = [
            matrix[i][j],
            matrix[i + 1][j],
            matrix[i + 2][j],
            matrix[i + 3][j]
        ]
        sum_vertical = math.prod(first_four_numbers)
        if sum_vertical > highest:
            highest = sum_vertical
            place = first_four_numbers
for i in range(20):
    for j in range(17):
        first_four_numbers = matrix[i][j:j+4]
        product = math.prod(first_four_numbers)
        if product > highest:
            highest = product
            place = first_four_numbers

for i in range(17):
    for j in range(20):
        first_four_numbers = [
            matrix[i][j],
            matrix[i + 1][j],
            matrix[i + 2][j],
            matrix[i + 3][j]
        ]
        product = math.prod(first_four_numbers)
        if product > highest:
            highest = product
            place = first_four_numbers

for i in range(17):
    for j in range(17):
        first_four_numbers = [
            matrix[i][j],
            matrix[i + 1][j + 1],
            matrix[i + 2][j + 2],
            matrix[i + 3][j + 3]
        ]
        product = math.prod(first_four_numbers)
        if product > highest:
            highest = product
            place = first_four_numbers

for i in range(17):
    for j in range(3, 20):
        first_four_seconds = [
            matrix[i][j],
            matrix[i + 1][j - 1],
            matrix[i + 2][j - 2],
            matrix[i + 3][j - 3]
        ]
        product = math.prod(first_four_seconds)
        if product > highest:
            highest = product
            place = first_four_seconds

print(highest, place)