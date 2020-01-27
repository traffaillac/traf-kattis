a, b, c, n = (int(i) for i in input().split())
print('YES' if a+b+c>=n>=3 and min(a, b, c)>=1 else 'NO')