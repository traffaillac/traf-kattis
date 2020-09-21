from heapq import heappush, heappop

n = int(input())
V = []
counts = [0] * (n+2)
for _ in range(n):
	v = int(input())
	V.append(v)
	counts[v] += 1
avail = []
for v, c in enumerate(counts):
	if c == 0:
		heappush(avail, v)
U = []
for v in V:
	print(v, avail)
	if not avail:
		print("Error")
		exit()
	U.append(heappop(avail))
	counts[v] -= 1
	if counts[v] == 0:
		heappush(avail, v)
print("\n".join(map(str, U)))
