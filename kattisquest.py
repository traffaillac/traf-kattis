# Balanced tree that is simple and fast in practice
from bisect import bisect, bisect_left
class BTree:
	def __init__(self, capacity=512):
		self.nodes = [[]]
		self.capacity = capacity
	def __len__(self):
		return sum(len(n) for n in self.nodes)
	def __iter__(self):
		for n in self.nodes:
			for k in n:
				yield k
	def __reversed__(self):
		for n in reversed(self.nodes):
			for k in reversed(n):
				yield k
	def __repr__(self):
		return f"[{', '.join(self)}]"
	
	def add(self, key, overwrite=None): # use None for a multiset
		N, C = self.nodes, self.capacity
		i, n = next(((i, n) for i, n in enumerate(N) if n and n[-1]>=key), (len(N)-1, N[-1]))
		j = bisect(n, key)
		# use tuples for keys and update this equality to turn the set into a map
		if j > 0 and n[j-1] == key and overwrite is not None:
			n[j] = key if overwrite else n[j]
			return overwrite
		if len(n) == C:
			N[i] = n[C//2:]
			N.insert(i, n[:C//2])
			n, j = (N[i], j) if j<=C//2 else (N[i+1], j-C//2)
		n.insert(j, key)
		return True
	def get_lower(self, key, default=None, delete=False):
		n = next((n for n in reversed(self.nodes) if n and n[0]<=key), [])
		j = bisect(n, key) - 1
		return default if j<0 else n.pop(j) if delete else n[j]
	def get_upper(self, key, default=None, delete=False):
		n = next((n for n in self.nodes if n and n[-1]>=key), [])
		j = bisect_left(n, key)
		return default if j==len(n) else n.pop(j) if delete else n[j]



# corner case: multiple identical quests
quests = BTree()
for _ in range(int(input())):
	comm, *args = input().split()
	if comm == "add":
		E, G = int(args[0]), int(args[1])
		quests.add(E * 100001 + G)
	elif comm == "query":
		X = int(args[0])
		gold = 0
		while True:
			key = quests.get_lower(X * 100001 + 100000, delete=True)
			if key is None: break
			E, G = key // 100001, key % 100001
			X -= E
			gold += G
		print(gold)
