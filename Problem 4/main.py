"""
Problem Statement: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99. find the largest palindrome made from the product of two 3-digit numbers.
"""

num1 = 100
num2 = 100
biggest = None
for i in range(100, 1000):
    for j in range(100, 1000):
        calc = i * j
        if str(calc) == str(calc)[::-1]:
            num1 = i
            num2 = j
            biggest = calc if biggest is None or calc > biggest else biggest
print(f"{num1} * {num2} = {biggest}")
