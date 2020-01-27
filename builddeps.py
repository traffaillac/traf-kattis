from sys import setrecursionlimit
setrecursionlimit(100000)

N = int(input())
rules = {}
# None-inexploré, False-inchangé, True-recompilé
states = {}
for n in range(N):
	f, *deps = input().split()
	f = f[:-1]
	rules[f] = deps
	states[f] = None
c = input()

def visit(f):
	deps = rules[f]
	s = states[f]
	# print('visit %s (%s)'%(f, s))
	if s == None:
		s = f == c
		for d in deps:
			s |= visit(d)
		states[f] = s
		if s:
			print(f)
	# print('return %s -> %s'%(f, s))
	return s

for f in rules:
	if states[f] == None:
		visit(f)
