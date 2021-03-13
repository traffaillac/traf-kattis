N, P = map(int, input().split())
X = [int(i) for i in input().split()]
X.sort()
excess = max(P*(i+1)-x for i, x in enumerate(X))
print(X[0]+excess)
