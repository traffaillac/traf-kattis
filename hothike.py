input()
T = [int(t) for t in input().split()]
t, d = min((max(a,b),d+1) for d,(a,b) in enumerate(zip(T,T[2:])))
print(d, t)