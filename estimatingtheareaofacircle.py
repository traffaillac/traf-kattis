from math import pi
while True:
    r, m, c = input().split()
    if r==m==c=='0': break
    print(pi*float(r)**2, (float(r)*2)**2*int(c)/int(m))