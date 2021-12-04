from sys import stdin

def main():
	for _ in range(int(next(stdin))):
		N = int(next(stdin))
		colors = next(stdin).split()
		adj = [[True] * N for _ in range(N)]
		for _ in range(int(next(stdin))):
			c1, c2 = map(lambda c: colors.index(c), next(stdin).split())
			adj[c1][c2] = adj[c2][c1] = False
		seq, last, count, fav = [0] * N, 0, 0, None
		while last >= 0:
			valid = last==0 or seq.index(seq[last])==last and adj[seq[last-1]][seq[last]]
			# if sequence is valid and length is N, save it
			if valid and last == N-1:
				count += 1
				if fav == None:
					fav = tuple(seq)
			# if sequence is valid and length is not N, append 0
			if valid and last < N-1:
				last += 1
				seq[last] = 0
			# if sequence is invalid or length is N, increment last and pop until valid
			else:
				seq[last] += 1
				while seq[last] == N:
					last -= 1
					if last < 0: break
					seq[last] += 1
		print(count)
		print(' '.join(colors[f] for f in fav))

main()
