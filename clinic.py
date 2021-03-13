from sys import stdin
from heapq import heappush, heappop

# possible case: patient name left before arriving
N, K = map(int, stdin.readline().split())
heap = []
left = set()
for _ in range(N):
	Q, T, *rest = stdin.readline().split()
	if Q == '1':
		heappush(heap, (int(T)*K-int(rest[1]), rest[0]))
		left.discard(rest[0])
	elif Q == '2':
		while heap:
			_, M = heappop(heap)
			if M not in left:
				print(M)
				break
		else:
			print('doctor takes a break')
	else:
		left.add(rest[0])
