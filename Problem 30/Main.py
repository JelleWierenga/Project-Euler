total_list = []
for i in range(2, 9**5 * 6):
    i = str(i)
    lijst = []
    for char in i:
        number = int(char)**5
        lijst.append(number)
    if i == str(sum(lijst)) and int(i) > 1:
        print("Nummer ^5", lijst)
        print("total", sum(lijst))
        print("lijst", total_list)
        total_list.append(sum(lijst))
        print("\n")

print(sum(total_list))
