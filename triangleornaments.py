from math import *
r = 0
for _ in range(int(input())):
	a, b, c = map(int, input().split())
	# 1. calcul de la médiane (http://villemin.gerard.free.fr/GeomLAV/Triangle/Propriet/Mediane0.htm)
	# 2. hauteur du demi-triangle (http://villemin.gerard.free.fr/GeomLAV/Triangle/Calcul/RelQuelh.htm#formule)
	r += sqrt(b*b-(3*b*b-c*c+a*a)**2/(8*b*b-4*c*c+8*a*a))*2
print(r)