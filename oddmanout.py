from collections import Counter
for x in range(1, int(input())+1):
    input()
    C = input().split()
    print(f"Case #{x}:", next(c for c, n in Counter(C).items() if n==1))