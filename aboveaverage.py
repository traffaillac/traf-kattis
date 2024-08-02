for _ in range(int(input())):
	G = [*map(int, input().split()[1:])]
	av = sum(G)/len(G)
	print(f"{sum(g>av for g in G)/len(G)*100:.3f}%")