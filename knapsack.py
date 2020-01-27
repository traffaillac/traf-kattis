try:
	while True:
		C, N = (int(x) for x in input().split())
		items = []
		for n in range(N):
			items.append(tuple(int(x) for x in input().split()))
		items.sort(key=lambda t: t[0] / t[1])
		
		highest_value = [-1] * 2001
		highest_value[0] = 0
		backtrack = [0] * 2001
		for n in range(N):
			for w0 in range(C - items[n][1], -1, -1):
				if highest_value[w0] < 0:
					continue
				w1 = w0 + items[n][1]
				v = highest_value[w0] + items[n][0]
				if highest_value[w1] < v:
					highest_value[w1] = v
					backtrack[w1] = backtrack[w0] | 1 << n
		
		for w in range(C, -1, -1): # il est possible qu'aucun item ne passe
			if highest_value[w] >= 0:
				print(bin(backtrack[w]).count('1'))
				for n in range(N):
					if backtrack[w] & 1 << n != 0:
						print(n, end=' ')
				print()
				break
except EOFError:
	pass
