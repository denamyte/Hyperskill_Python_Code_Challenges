def contains_upto_permutations(text, pattern):
    for letter in set(pattern):
        if pattern.count(letter) > text.count(letter):
            return False
    return True


print(contains_upto_permutations(input(), input()))
