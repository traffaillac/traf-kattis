B = {}
for _ in range(int(input())):
    S, C, D = input().split()
    if D not in B or int(C)>B[D][1]:
        B[D] = (S, int(C))
print(len(B))
print('\n'.join(sorted(S for S, C in B.values())))
