cache_counter = [0]


def fib(n):
    numbers: dict = {}
    return fib_helper(n, numbers)


def fib_helper(n, numbers):
    if numbers.get(n) is not None:
        cache_counter[0] += 1
        return numbers[n]
    if n < 2:
        numbers[n] = n
    else:
        numbers[n] = fib_helper(n - 1, numbers) + fib_helper(n - 2, numbers)

    return numbers[n]


print(fib(6))
print(cache_counter[0])
