import math
#grid is n * n where n = 20

x, y = 20, 20

sum = math.factorial(x + y) // (math.factorial(x) * math.factorial(y))
print(sum)
