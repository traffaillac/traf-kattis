input()
A = [*map(int, input().split())]
print(max(((a, i+1) for i, a in enumerate(A) if A.count(a)==1), default=[0,"none"])[1])