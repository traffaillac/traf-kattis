N = int(input())
S = input()
i = 0
for _ in range(N):
    i = max(S.index('R',i),S.index('G',i),S.index('B',i))+1
    print(S[i-1],end='')
print()