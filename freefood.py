d = set()
for _ in range(int(input())):
    s, t = map(int, input().split())
    d |= set(range(s, t+1))
print(len(d))
