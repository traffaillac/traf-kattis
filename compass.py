n1 = int(input())
n2 = int(input())
cw = (n2-n1)%360
ccw = (n1-n2)%360
print(cw if cw<=ccw else -ccw)