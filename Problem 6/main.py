"""
Problem statement: The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_sqrt = []

def sum_of_squares(n):
    for i in range(n + 1):
        calc = i ** 2
        sum_sqrt.append(calc)
    total = sum(sum_sqrt)
    return total

total_sum_squares = sum_of_squares(100)

sqrt_sum = []

def square_of_sum(n):
    for i in range(n + 1):
        sqrt_sum.append(i)
    total1 = sum(sqrt_sum) ** 2
    return total1

total_square_sum = square_of_sum(100)

print(total_square_sum - total_sum_squares)