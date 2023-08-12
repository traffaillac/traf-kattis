G, T, N = map(int, input().split())
W = sum(map(int, input().split()))
print((G-T)//10*9-W)
