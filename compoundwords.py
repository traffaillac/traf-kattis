from itertools import permutations
from sys import stdin

comp = set(t[0]+t[1] for t in permutations(stdin.read().split(), 2))
print("\n".join(sorted(comp)))
