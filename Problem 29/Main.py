store = []
for i in range(2, 101):
    for j in range(2, 101):
        print(f"{i}^{j} = {i**j}")
        store.append(i**j)
        # print(i**j)

print(len(list(set(store))))
