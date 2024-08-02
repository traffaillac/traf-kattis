# golfed even further afterwards :)
from bisect import bisect

n, k = map(int, input().split())
S = set()
for _ in range(n):
	H = []
	A = []
	for a in map(int, input().split()):
		i = bisect(A, a)
		H.insert(i, max(H[max(i-1,0):i+1], default=-1)+1)
		A.insert(i, a)
	S.add(tuple(H))
print(len(S))