def f(graph, labs, deps, lab):
	stacks = [[n for n,(d,l) in enumerate(zip(deps, labs)) if d==0 and l==0],
	          [n for n,(d,l) in enumerate(zip(deps, labs)) if d==0 and l==1]]
	count = -1
	while stacks[0] or stacks[1]:
		while stacks[lab]:
			n = stacks[lab].pop()
			for m in graph[n]:
				deps[m] -= 1
				if deps[m] == 0:
					stacks[labs[m]].append(m)
		lab ^= 1
		count += 1
	return count

for _ in range(int(input())):
	N, M = map(int, input().split())
	labs = [int(i)-1 for i in input().split()]
	deps = [0] * N
	graph = [[] for _ in range(N)]
	for _ in range(M):
		i, j = (int(n)-1 for n in input().split())
		graph[i].append(j)
		deps[j] += 1
	copy = deps[:]
	print(min(f(graph, labs, deps, 0), f(graph, labs, copy, 1)))
