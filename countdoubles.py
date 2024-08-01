n, m = map(int, input().split())
A = list(map(int, input().split()))
print(sum(sum(a%2==0 for a in A[i:i+m])>=2 for i in range(n-m+1)))