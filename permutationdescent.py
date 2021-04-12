# PDC(N, v) = 
mem = {}
def PDC(N, v):
	if v==0 or v==N-1:
		return 1
	if (N, v) in mem:
		return mem[N, v]
	c = (PDC(N-1, v-1) * (N-v) + PDC(N-1, v) * (v+1)) % 1001113
	mem[N, v] = c
	return c

for _ in range(int(input())):
	K, N, v = map(int, input().split())
	print(K, PDC(N, v))
