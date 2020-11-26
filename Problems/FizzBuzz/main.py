fizz_buzz_dict = {15: "FizzBuzz",
                  5: "Buzz",
                  3: "Fizz"}
for num in range(1, 101):
    result = num
    for key in fizz_buzz_dict:
        if num % key == 0:
            result = fizz_buzz_dict[key]
            break
    print(result)
