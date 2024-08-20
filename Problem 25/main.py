A = 1
B = 1

for i in range(100000):
    som = A + B
    A = B
    B = som
    if len(str(som)) == 1000:
        print(f"f{i+3} = {som}")
        break
