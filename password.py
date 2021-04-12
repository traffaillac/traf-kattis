N = int(input())
probs = [float(input().split()[1]) for _ in range(N)]
probs.sort(reverse=True)
print(sum((i+1)*p for i, p in enumerate(probs)))
