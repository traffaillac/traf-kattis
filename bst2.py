# Balanced and order statistic tree that is simple and fast in practice
class BTree:
	def __init__(self, capacity=2048):
		self.nodes = [[]]
		self.capacity = capacity
	def __len__(self):
		return sum(len(n) for n in self.nodes)
	def __iter__(self):
		for n in self.nodes:
			for p in n:
				yield p # tuple (key, value)
	def __reversed__(self):
		for n in reversed(self.nodes):
			for p in reversed(n):
				yield p
	
	def get(self, key, default=None):
		n = next((n for n in self.nodes if n and n[-1][0]>=key), [])
		return next((p[1] for p in n if p[0]==key), default)
	def get_lower(self, key, default=(None, None)):
		n = next((n for n in reversed(self.nodes) if n and n[0][0]<=key), [])
		return next((p for p in reversed(n) if p[0]<=key), default)
	def get_upper(self, key, default=(None, None)):
		n = next((n for n in self.nodes if n and n[-1][0]>=key), [])
		return next((p for p in n if p[0]>=key), default)
	def insert(self, key, value, overwrite=True):
		N, C = self.nodes, self.capacity
		i, n = next(((i, n) for i, n in enumerate(N) if n and n[-1][0]>=key), (len(N)-1, N[-1]))
		j, k = next(((j, p[0]) for j, p in enumerate(n) if p[0]>=key), (len(n), None))
		if k == key:
			n[j] = (key, value) if overwrite else n[j]
			return overwrite, n[j][1]
		if len(n) == C:
			N[i] = n[C//2:]
			N.insert(i, n[:C//2])
			n, j = (N[i], j) if j<=C//2 else (N[i+1], j-C//2)
		n.insert(j, (key, value))
		return True, value


# TLE on Kattis, but about 2x too slow which is not too bad
depths = BTree()
C = 0
for _ in range(int(input())):
	i = int(input())
	d = max(depths.get_lower(i, (0, 0))[1], depths.get_upper(i, (0, 0))[1])
	depths.insert(i, d + 1)
	C += d
	print(C)
