N = input()
M = input()
N = '0'*max(len(M)-len(N),0)+N
M = '0'*max(len(N)-len(M),0)+M
A = ''.join(n for n, m in zip(N, M) if n>=m)
B = ''.join(m for n, m in zip(N, M) if m>=n)
print(int(A) if A else "YODA")
print(int(B) if B else "YODA")