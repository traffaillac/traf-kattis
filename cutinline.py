def main():
    Q = [input() for _ in range(int(input()))]
    for _ in range(int(input())):
        e, *n = input().split()
        if e == "cut":
            Q.insert(Q.index(n[1]), n[0])
        else:
            Q.remove(n[0])
    print('\n'.join(Q))
main()