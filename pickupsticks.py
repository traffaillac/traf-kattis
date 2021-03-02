N, M = map(int, input().split())
graph = [[] for _ in range(N)]
parents = [0] * N
for _ in range(M):
	a, b = (int(i)-1 for i in input().split())
	graph[a].append(b)
	parents[b] += 1
stack = [n for n,p in enumerate(parents) if p==0]
cur = 0
while cur < len(stack):
	n = stack[cur]
	for m in graph[n]:
		parents[m] -= 1
		if parents[m] == 0:
			stack.append(m)
	cur += 1
print("IMPOSSIBLE" if len(stack)<N else "\n".join(str(n+1) for n in stack))
