attr = input().split()
m = int(input())
songs = [input().split() for _ in range(m)]
n = int(input())
for i in range(n):
	if i > 0: print()
	a = attr.index(input())
	songs.sort(key=lambda t:t[a])
	print(*attr)
	for s in songs:
		print(*s)
