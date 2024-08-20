# print(1/3)
longest = ""


for i in range(2, 1001):
    som = 1/i
    # print(som)
    string = str(som)
    string = string[2:]
    numbers = list(string)
    # print(numbers)

    for num in range(len(numbers) - 1):
        if numbers[num] == numbers[num + 1]:
            # print(f"1/{i} = {som}")
            if len(string) > len(longest):
                longest = string
            break

print(longest)