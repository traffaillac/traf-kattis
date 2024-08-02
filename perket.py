from functools import reduce
from operator import mul
N = int(input())
I = [[*map(int, input().split())] for _ in range(N)]
d = 1000000000
for p in range(1, 2**N):
	s = reduce(mul, (s for i,(s,_) in enumerate(I) if p&1<<i), 1)
	b = sum(b for i,(_,b) in enumerate(I) if p&1<<i)
	d = min(d, abs(s-b))
print(d)