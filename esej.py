from itertools import product, islice
from string import ascii_lowercase

A, B = map(int, input().split())
words = []
words = ["".join(t) for t in islice(product(ascii_lowercase, repeat=4), B)]
print(" ".join(words))
