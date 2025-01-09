triangle = {}
pentagon = {}
hexagon = {}

for i in range(1, 100000):
    Triangle = int(i * (i + 1) / 2)
    triangle.update({Triangle: i})
    Hexagon = int(i * (2 * i - 1))
    hexagon.update({Hexagon: i})
    Pentagon = int(i * (3 * i - 1) / 2)
    pentagon.update({Pentagon: i})

for key in triangle:
    if key == 1:
        continue
    if key in pentagon and key in hexagon:
        print(key)
        print("\n")
        continue