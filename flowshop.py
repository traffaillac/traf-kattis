N, M = (int(i) for i in input().split())
avail = [0] * M
ends = []
for _ in range(N):
	time = 0
	for i, p in enumerate(map(int, input().split())):
		time = max(time, avail[i]) + p
		avail[i] = time
	ends.append(time)
print(" ".join(map(str, ends)))