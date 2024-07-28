N, M, Q = map(int, input().split())
chars = [input() for _ in range(N)]
C = ['?']*M
for _ in range(Q):
    a, c = input().split()
    C[int(a)-1] = c
C = ''.join(C)
sols = [i for i, char in enumerate(chars) if all(a==b or b=='?' for a, b in zip(char, C))]
print(f"unique\n{sols[0]+1}" if len(sols)==1 else f"ambiguous\n{len(sols)}")