b = set()
for _ in range(int(input())):
    d, n = input().split()
    if d=="entry":
        a = n in b
        b.add(n)
    else:
        a = n not in b
        b.discard(n)
    print(n, ("entered" if d=="entry" else "exited")+(" (ANOMALY)" if a else ''))