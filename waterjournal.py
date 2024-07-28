n, a, b = map(int, input().split())
W = [int(input()) for _ in range(n-1)]
m, M = min(W), max(W)
print('\n'.join(map(str, range(a, b+1))) if m==a and M==b else -1 if a<m<=M<b else a if a<m else b)