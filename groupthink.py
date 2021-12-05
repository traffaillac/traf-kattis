from itertools import product

n = int(input())
M = [[0] * n for _ in range(n)]
for _ in range(n * n):
	i, j, k = map(int, input().split())
	M[i][j] = k
P1 = all(M[M[i][j]][k]==M[i][M[j][k]] for i, j, k in product(range(n), repeat=3))
P2, I = next(((True,i) for i in range(n) if all(M[i][j]==M[j][i]==j for j in range(n))), (False,None))
P3 = False if I==None else all(any(M[i][j]==M[j][i]==I for j in range(n)) for i in range(n))
print("magma" if not P1 else "semigroup" if not P2 else "monoid" if not P3 else "group")
