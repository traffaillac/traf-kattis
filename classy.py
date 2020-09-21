tk = {"lower": 1, "middle": 0, "upper": -1}
T = int(input())
for _ in range(T):
	people = []
	n = int(input())
	for _ in range(n):
		name, cl, _ = input().split()
		cl = list(map(lambda c: tk[c], cl.split("-")[::-1]))
		people.append((cl+[0]*(10-len(cl)), name[:-1]))
	people.sort()
	for cl, name in people:
		print(name)
	print("==============================")
