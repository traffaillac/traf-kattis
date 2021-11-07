L, H = map(int, input().split())
count = 0
for c in range(L, H+1):
	s = str(c)
	count += '0' not in s and len(set(s)) == 6 and all(c % int(i) == 0 for i in s)
print(count)
