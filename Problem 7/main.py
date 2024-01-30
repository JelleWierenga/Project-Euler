def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def get_prime_num(N):
    counter = 0
    current_num = 1

    while counter < N:
        current_num += 1
        if is_prime(current_num):
            counter += 1

    return current_num


# Example usage
N = 10001
nth_prime = get_prime_num(N)
print(f"The {N}th prime number is: {nth_prime}")