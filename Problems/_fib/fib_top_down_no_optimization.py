calls_counter = [0]


def fib(n):
    if n == 1:
        calls_counter[0] += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(6))
print(calls_counter)
