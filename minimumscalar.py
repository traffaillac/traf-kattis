for t in range(int(input())):
    input()
    X = sorted(map(int, input().split()))
    Y = sorted(map(int, input().split()))
    print(f"Case #{t+1}:", sum(x*y for x, y in zip(X, reversed(Y))))