while True:
	n = int(input())
	if n == 0: break
	boxes = []
	for i in range(n):
		x1, y1, x2, y2, t = input().split()
		boxes.append((float(x1), float(y1), float(x2), float(y2), t))
	m = int(input())
	for i in range(m):
		x, y, t = input().split()
		x, y = float(x), float(y)
		box = next((b[4] for b in boxes if b[0]<=x<=b[2] and b[1]<=y<=b[3]), 'floor')
		print(t, 'correct' if box == t else box)
	print()
