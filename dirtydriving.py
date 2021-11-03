_, p = map(int, input().split())
distances = [int(d) for d in input().split()]
distances.sort()
delta = max(p * (i + 1) - d for i, d in enumerate(distances))
print(distances[0] + delta)
