N, W, H = map(int, input().split())
for n in range(N):
	i = int(input())
	print('DA' if i*i <= W*W + H*H else 'NE')
