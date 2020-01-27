while True:
	n = int(input())
	if n < 0:
		break
	graph = []
	for i in range(n):
		graph.append([int(x) for x in input().split()])
	weaks = []
	for i in range(n):
		weak = True
		for j in range(n):
			if graph[i][j] == 0:
				continue
			for k in range(n):
				if graph[i][k] == 1 and graph[j][k] == 1:
					weak = False
		if weak:
			weaks.append(i)
	print(' '.join(map(str, weaks)))
