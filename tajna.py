W = input()
N = len(W)
R, C = next((N//C, C) for C in range(1, N+1) if N%C==0 and N//C<=C)
print(''.join(W[c*R+r] for r in range(R) for c in range(C)))