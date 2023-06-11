def fib_bottom_up(n):
    if n < 2:
        return n

    prev_1 = 0
    prev_2 = 1
    result = 0

    for i in range(2, n + 1):
        result = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = result

    return result


print(fib_bottom_up(0))
print(fib_bottom_up(1))
print(fib_bottom_up(2))
print(fib_bottom_up(3))
print(fib_bottom_up(4))
print(fib_bottom_up(5))
print(fib_bottom_up(6))
print(fib_bottom_up(7))
print(fib_bottom_up(8))
