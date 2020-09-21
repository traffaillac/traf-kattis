T = int(input())
for t in range(1, T+1):
	N, K = (int(i) for i in input().split())
	print(f"Case #{t}:", "ON" if K%2**N == 2**N-1 else "OFF")
