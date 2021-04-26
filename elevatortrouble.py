from collections import deque

def main():
	f, s, g, u, d = map(int, input().split())
	floors = {s-1: 0}
	fifo = deque((s-1,))
	while fifo:
		floor = fifo.popleft()
		if floor == g-1:
			print(floors[floor])
			break
		if floor+u < f and floor+u not in floors:
			floors[floor+u] = floors[floor]+1
			fifo.append(floor+u)
		if floor-d >= 0 and floor-d not in floors:
			floors[floor-d] = floors[floor]+1
			fifo.append(floor-d)
	else:
		print("use the stairs")

main()
