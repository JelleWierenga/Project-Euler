"""
Problem Statement: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99. find the largest palindrome made from the product of two 3-digit numbers.
"""

num1 = 100
num2 = 100

for i in range(num1 + num2):
    num1, num2 = (num1, num2 + 1) if num1 > num2 else (num1 + 1, num2)
    calc = num1 * num2
    if str(calc) == str(calc)[::-1]:
        print(f"{num1} * {num2} = {calc}")
        break
