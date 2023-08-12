N, P, S = map(int, input().split())
C = set(range(1, N+1))
for _ in range(S):
    L = set(map(int, input().split()[1:]))
    if P in L:
        print("KEEP")
        C = L
    else:
        print("REMOVE")
        C -= L
