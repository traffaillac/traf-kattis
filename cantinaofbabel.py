largest = 0
# graph is a list/dict of adjacency lists, index and low are None-initialized arrays
def tarjan_scc(graph, index, low, i, uuid=0, stack=[]):
	global largest
	index[i] = low[i] = uuid
	stack.append(i) # condition for i being on stack is index[i]!=None!=low[i]
	for j in graph[i]:
		if j not in index: # node was never visited before
			uuid = tarjan_scc(graph, index, low, j, uuid+1, stack)
		if j in low: # node was not visited by another SCC
			low[i] = min(low[i], low[j])
	if index[i] == low[i]:
		size = 0
		while True:
			j = stack.pop()
			del low[j]
			size += 1
			if j == i:
				break
		largest = max(largest, size)
	return uuid

listeners = {}
characters = []
N = int(input())
for _ in range(N):
	name, *understands = input().split()
	characters.append((name, understands[0]))
	for lang in understands:
		listeners.setdefault(lang, []).append(name)
graph = {}
for name, lang in characters:
	graph[name] = listeners.get(lang, [])

index = {}
low = {}
for name in graph:
	if name not in index:
		tarjan_scc(graph, index, low, name)
print(N - largest)
