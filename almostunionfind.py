def set_find(s, i):
	if type(s[i]) == int:
		s[i] = i = set_find(s, s[i])
	return i
def set_union(s, i, j):
	i = set_find(s, i)
	j = set_find(s, j)
	if i != j:
		if s[i][0] < s[j][0]:
			i, j = j, i
		s[i][0] += s[j][0]
		s[i][1] += s[j][1]
		s[j] = i



try:
	while True:
		N, M = map(int, input().split())
		s = [[1, i + 1] for i in range(N)]
		e = [i - 1 for i in range(N + 1)]
		for m in range(M):
			c, p, *q = (int(i) for i in input().split())
			if c == 1:
				set_union(s, e[p], e[q[0]])
			elif c == 2 and set_find(s, e[p]) != set_find(s, e[q[0]]):
				t = s[set_find(s, e[p])]
				t[0] -= 1
				t[1] -= p
				e[p] = len(s)
				s.append([1, p])
				set_union(s, e[p], e[q[0]])
			elif c == 3:
				t = s[set_find(s, e[p])]
				print(t[0], t[1])
except EOFError:
	pass
