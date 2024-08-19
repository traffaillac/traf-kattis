from itertools import combinations
from math import prod

N = [*map(int, input().split())]
K = int(input())
print(sum(prod(c) for c in combinations(N, K)))