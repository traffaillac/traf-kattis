import math

def dist(a, b):
	return math.hypot(a % 3 - b % 3, a // 3 - b // 3)

grid = [int(i) for i in input().split()]
grid.extend(int(i) for i in input().split())
grid.extend(int(i) for i in input().split())
length = 0
for i in range(1, 9):
	length += dist(grid.index(i), grid.index(i + 1))
print(length)
