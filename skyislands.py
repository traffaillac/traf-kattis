# Union-Find (on array initialized with -1)
def set_find(s:list, i:int):
	while s[i] >= 0:
		i = s[i]
	return i
def set_union(s:list, i:int, j:int):
	i = set_find(s, i)
	j = set_find(s, j)
	if i != j:
		if -s[i] < -s[j]:
			i, j = j, i
		s[i] += s[j]
		s[j] = i

N, M = map(int, input().split())
S = [-1]*N
for _ in range(M):
	a, b = map(int, input().split())
	set_union(S, a-1, b-1)
print("YES" if S[set_find(S,0)]==-N else "NO")