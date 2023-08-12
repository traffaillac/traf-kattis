n = 0
for r in input().split(';'):
    if '-' in r:
        a, b = map(int, r.split('-'))
        n += b-a+1
    else:
        n += 1
print(n)
