from math import tan, pi
for _ in range(int(input())):
    n, l, d, g = map(int, input().split())
    a = n*l*l/4/tan(pi/n) + d*g*(n*l+d*g*pi)
    print(a)
