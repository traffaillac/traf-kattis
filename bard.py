N = int(input())
E = int(input())
known = [0] * N
next_song = 0
for e in range(E):
	K = [int(i) for i in input().split()][1:]
	if 1 in K:
		for k in K:
			known[k - 1] |= 1 << next_song
		next_song += 1
	else:
		share = 0
		for k in K:
			share |= known[k - 1]
		for k in K:
			known[k - 1] = share
for n, k in enumerate(known):
	if k == (1 << next_song) - 1:
		print(n + 1)
