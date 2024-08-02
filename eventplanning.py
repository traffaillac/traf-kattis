N, B, H, W = map(int, input().split())
b = B+1
for _ in range(H):
	p = int(input())
	if any(a>=N for a in map(int, input().split())):
		b = min(b, N*p)
print(b if b<=B else "Stay home")