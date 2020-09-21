N, M = (int(i) for i in input().split())
moves = [input() for _ in range(N)]
print(1+sum(all(m[c]=='_' for m in moves) for c in range(M)))
