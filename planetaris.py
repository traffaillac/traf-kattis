n, a = map(int, input().split())
w = 0
for e in sorted(map(int, input().split())):
	if a > e:
		a -= e+1
		w += 1
print(w)