from math import sqrt


def is_prime(n):  # it's much better to have a clear function without side effects
    if n <= 1:
        return False
    for i in range(2, 1 + round(sqrt(n))):
        if n % i == 0:
            return False
    return True


print('This number is prime' if is_prime(int(input())) else 'This number is not prime')
