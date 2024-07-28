while True:
    w = float(input().split()[2])
    if w==0: break
    X = [-w/2] + sorted(map(float, input().split())) + [75+w/2]
    Y = [-w/2] + sorted(map(float, input().split())) + [100+w/2]
    print("YES" if all(b-a<=w for a,b in zip(X,X[1:])) and all(b-a<=w for a,b in zip(Y,Y[1:])) else "NO")