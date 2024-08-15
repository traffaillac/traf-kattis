from math import comb

N = int(input())
print(sum(comb(N,k) for k in range(2, N+1)))