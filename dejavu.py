N = int(input())
points = []
numX = [0] * 100001
numY = [0] * 100001
for _ in range(N):
	X, Y = map(int, input().split())
	points.append((X, Y))
	numX[X] += 1
	numY[Y] += 1
triangles = 0
for X, Y in points:
	triangles += (numX[X] - 1) * (numY[Y] - 1)
print(triangles)
