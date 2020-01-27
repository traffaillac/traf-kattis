from sys import stdin

# edge cases:
# _ asking a city with no outgoing edges
# _ two independent subgraphs
N = int(input())
cities = {}
for n in range(N):
	orig, dst = stdin.readline().split()
	cities.setdefault(orig, []).append(dst)
	cities.setdefault(dst, [])

# None-unknown, True-safe/marked, False-trapped
safe = {}
def visit(c):
	s = safe.get(c)
	if s == None:
		safe[c] = True
		s = False
		for dst in cities[c]:
			s |= visit(dst)
		safe[c] = s
	return s

for l in stdin:
	l = l.rstrip()
	print('%s %s'%(l, 'safe' if visit(l) else 'trapped'))
