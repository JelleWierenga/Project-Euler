Letter_Number = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

with open("words.txt", "r") as f:
    words = f.read().replace('"', '').split(',')
    Word_Sum = {}
    for word in words:
        store = []
        for letter in word:
            store.append(Letter_Number[letter])
        print(word)
        print(sum(store))
        Word_Sum.update({word: sum(store)})
    print(Word_Sum)


total = 0
for i in range(1, len(Word_Sum)):
    formula = int(0.5 * i * (i + 1))
    matching_words = []
    for word, value in Word_Sum.items():
        if value == formula:
            matching_words.append(word)

    if matching_words:
        print(f"Triangulair getal: {formula}, Woorden: {', '.join(matching_words)}")
        print(len(matching_words))
        total += len(matching_words)

print(total)