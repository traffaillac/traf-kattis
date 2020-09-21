N = int(input())
names = [input() for _ in range(N)]
print("INCREASING" if names == sorted(names) else "DECREASING" if names == sorted(names, reverse=True) else "NEITHER")
