# I'm REALLY lazy on the complexity of this one
from itertools import product
V = int(input())
divs = [d for d in range(1, V+1) if V%d==0]
print(2 * min(a*b+a*c+b*c for a,b,c in product(divs, repeat=3) if a*b*c==V))
