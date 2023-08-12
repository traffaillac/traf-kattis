n = int(input())
Q = [1] * n
for i, d in enumerate(map(int, input().split())):
    Q[d+1] = i+2
print(*Q)