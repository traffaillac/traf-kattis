N = int(input())
sections = [int(i) for i in input().split()]
accum = [0] * (N+1)
for i in range(N):
	accum[i+1] = accum[i] + sections[i]
try:
	assert accum[N]%3 == 0
	print(accum.index(accum[N]//3), accum.index(accum[N]//3*2))
except:
	print(-1)
