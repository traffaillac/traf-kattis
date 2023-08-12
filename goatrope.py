from math import hypot
x, y, x1, y1, x2, y2 = map(int, input().split())
print(max(y-y2, y1-y) if x1<=x<=x2 else max(x-x2, x1-x) if y1<=y<=y2 else min(hypot(x-x1, y-y1), hypot(x-x1, y-y2), hypot(x-x2, y-y1), hypot(x-x2, y-y2)))