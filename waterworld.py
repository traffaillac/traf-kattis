n, m = map(int, input().split())
print(sum(sum(map(int, input().split())) for _ in range(n))/(n*m))