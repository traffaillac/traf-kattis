from sys import stdin, stdout
input = stdin.readline

class DisjointSet:
	def __init__(self):
		self.parent = {}
		self.cardinal = {}
	def find(self, a):
		if a in self.parent:
			t = self.find(self.parent[a])
			self.parent[a] = t[0]
		else:
			t = a, self.cardinal.get(a, 1)
		return t
	def union(self, a, b):
		a, ca = self.find(a)
		b, cb = self.find(b)
		if a != b:
			if ca < cb:
				a, ca, b, cb = b, cb, a, ca
			self.parent[b] = a
			self.cardinal[a] = ca + cb

def main():
	n, q = map(int, input().split())
	S = DisjointSet()
	for _ in range(q):
		command, *args = input().split()
		if command == 't':
			S.union(int(args[0])-1, int(args[1])-1)
		else:
			stdout.write(f"{S.find(int(args[0])-1)[1]}\n")

main()
