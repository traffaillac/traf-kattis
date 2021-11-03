# graph is a list/dict of adjacency lists, index and low are None-initialized arrays
def tarjan_scc(graph, index, low, i, uuid=0, stack=[]):
	index[i] = low[i] = uuid
	stack.append(i) # condition for i being on stack is index[i]!=None!=low[i]
	for j in graph[i]:
		if index[j] == None: # node was never visited before
			uuid = tarjan_scc(graph, index, low, j, uuid+1, stack)
		if low[j] != None: # node was not visited by another SCC
			low[i] = min(low[i], low[j])
	if index[i] == low[i]:
		while True:
			j = stack.pop()
			low[j] = None
			print(j, end=' ')
			if j == i:
				break
		print()
	return uuid

for _ in range(int(input())):
	n, m = map(int, input().split())
	graph = [set() for _ in range(n)]
	for _ in range(m):
		x, y = (int(s)-1 for s in input().split())
		graph[x].add(y)
	tarjan_scc(graph, [None]*n, [None]*n, 0)
