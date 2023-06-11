# object_list = [1, 397, 27468, -95, 1309, [], 397, -539874, [], -240767, -95, 397]

filtered_hashable = filter(lambda el: isinstance(el, collections.Hashable), object_list)
hashes = map(hash, filtered_hashable)
counter = collections.Counter(hashes)
sum_more_than_1 = sum(filter(lambda v: v > 1, counter.values()))

print(sum_more_than_1)
