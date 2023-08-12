PDC = [[1], [1, 1]]
for N in range(3, 101):
	PDC.append([1] + [(PDC[-1][i-1]*(N-i)+PDC[-1][i]*(i+1))%1001113 for i in range(1, N-1)] + [1])
for _ in range(int(input())):
	K, N, v = map(int, input().split())
	print(K, PDC[N-1][v])
