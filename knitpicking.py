n = int(input())
lefts = {}
rights = {}
anys = {}
socks = {}
for _ in range(n):
	i, j, k = input().split()
	socks.setdefault(i, [0, 0, 0])[0 if j == "left" else 1 if j == "right" else 2] += int(k)
if all(l==a==0 or r==a==0 or a==1 for l, r, a in socks.values()):
	print("impossible")
else:
	print(sum(max(l, r, 1) for l, r, a in socks.values()) + 1)
