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

def main2():
	for _ in range(int(next(stdin))):
		N = int(next(stdin))
		colors = next(stdin).split()
		adj = [[True] * N for _ in range(N)]
		for _ in range(int(next(stdin))):
			c1, c2 = map(lambda c: colors.index(c), next(stdin).split())
			adj[c1][c2] = adj[c2][c1] = False
		counts = [[0] * N for _ in range(1 << N)]
		scores = [[(1 << 48) - 1] * N for _ in range(1 << N)]
		mask = (1 << N) - 1
		for i in range(N):
			counts[1 << i ^ mask][i] = 1
			scores[1 << i ^ mask][i] = i
		m = mask >> 2 # set bits are colors not painted yet
		while True:
			for i in range(N):
				if m & 1 << i: continue
				n = m | 1 << i
				# sum all paintings in n that can be completed with color i
				counts[m][i] = sum(counts[n][j] for j in range(N) if not n&1<<j and adj[i][j])
				scores[m][i] = min((scores[n][j]<<4|i for j in range(N) if not n&1<<j and adj[i][j]), default=(1<<48)-1)
			if m == 0: break
			# compute next bit permutation (http://graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation)
			t = m | (m - 1)
			m = (t + 1) & mask | (((~t & -~t) - 1) >> (m & -m).bit_length())
		print(sum(counts[0]))
		
		seq = min(scores[0])
		print(' '.join(colors[seq >> (i*4) & 15] for i in range(N-1,-1,-1)))

main2()
