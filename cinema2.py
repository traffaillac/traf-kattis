N, M = map(int, input().split())
G = list(map(int, input().split()))
n = 0
for i, g in enumerate(G):
    n += g
    if n>N:
        print(len(G)-i)
        exit()
print(0)