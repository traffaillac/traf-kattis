from collections import Counter
K = int(input().split()[1])
F = Counter(map(int, input().split()))
m = min(F[k] for k in range(1, K+1))
C = sorted(k for k in range(1, K+1) if F[k]==m)
print(len(C))
print(*C)