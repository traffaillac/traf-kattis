while True:
	n = int(input())
	if n==0: break
	B = [tuple(map(int, input().split())) for _ in range(n)]
	X, Y = B[len(B)//2]
	print(sum((x-X)*(y-Y)>0 for x, y in B), sum((x-X)*(y-Y)<0 for x, y in B))