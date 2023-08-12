from math import log10
for _ in range(int(input())):
    print(int(log10(max(float(input()), 1.0)))+1)