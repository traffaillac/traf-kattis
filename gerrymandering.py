P, D = map(int, input().split())
A, B = [0]*D, [0]*D
for _ in range(P):
    d, a, b = map(int, input().split())
    A[d-1] += a
    B[d-1] += b
Wa, Wb, V = 0, 0, 0
for a, b in zip(A, B):
    v = a + b
    V += v
    wa = a-v//2-1 if a>b else a
    wb = b-v//2-1 if b>a else b
    Wa += wa
    Wb += wb
    print('A' if a>b else 'B', wa, wb)
print(abs(Wa-Wb)/V)