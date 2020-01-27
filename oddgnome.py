for n in range(int(input())):
	g = [int(i) for i in input().split()[1:]]
	print(next(i+1 for i in range(1,len(g)-1) if g[i-1]<g[i+1] and not g[i-1]<g[i]<g[i+1]))