input()
T = sorted(map(int, input().split()))
Q = sorted(map(int, input().split()))
i = 0
n = 0
for t in T:
	while i<len(Q) and Q[i]<t:
		i += 1
	if i==len(Q):
		break
	n += 1
	i += 1
print(n)