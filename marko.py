from collections import Counter
d = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
C = Counter(''.join(str(d[ord(c)-97]) for c in input()) for _ in range(int(input())))
print(C[input()])