input()
angles = {0}
for n in map(int, input().split()):
	todo = list(angles)
	while todo:
		a = (todo.pop() + n) % 360
		if a not in angles:
			angles.add(a)
			todo.append(a)
for k in map(int, input().split()):
	print('YES' if k in angles else 'NO')
