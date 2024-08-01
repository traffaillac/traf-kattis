input()
F = [c/(i+1) for i, c in enumerate(sorted(map(int, input().split())))]
print("impossible" if max(F)>1 else min(F))