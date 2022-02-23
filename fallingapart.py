input()
A = list(sorted(map(int, input().split()), reverse=True))
print(sum(a for i, a in enumerate(A) if i%2==0), sum(a for i, a in enumerate(A) if i%2==1))
