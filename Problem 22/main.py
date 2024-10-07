file = open("0022_names.txt", "r")

for name in file:
    names = name.replace('"', '').split(",")
    names = sorted(names)
    print(names)


letters = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
    "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
    "W": 23, "X": 24, "Y": 25, "Z": 26
}

total_score = 0

# Loop through names with their index
for index, name in enumerate(names, start=1):
    score = sum(letters[letter] for letter in name)
    total_score += score * index  # Multiply score by position (index)

print(f"Total of all name scores: {total_score}")