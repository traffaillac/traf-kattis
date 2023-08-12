input()
A = sorted(map(int, input().split()))
print(sum(A)+A[0]*(len(A)-2))