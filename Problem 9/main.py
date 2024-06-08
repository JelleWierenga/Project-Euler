# a < b < c
# a + b + c = 1000
# a^2 + b^2 = c^2
# 3^2 + 4^2 = 5^2



for a in range(200, 1000):
    for b in range(200, 1000):
        for c in range(200, 1000):
            if a < b < c:
                if a**2 + b**2 == c**2 and a + b + c == 1000 and a < b < c:
                    print(f"{a} {b} {c} = {a + b + c}")
                    print(f"{a**2} {b**2}= {c**2}")
                    print(f"Product = {a * b * c}")
                    break