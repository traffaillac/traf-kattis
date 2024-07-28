n = int(input())
D = [int(input()) for _ in range(n)]
R = []
for k in range(2, n+1):
    x = n//k
    if n%k==0 and all(max(D[i*x:i*x+x])<min(D[i*x+x:i*x+x+x]) for i in range(k-1)):
        R.append(str(k))
print('\n'.join(R) if R else -1)