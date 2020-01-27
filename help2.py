# Union-Find (begin with a None initialised array)
def set_find(s, i):
	if type(s[i]) == int:
		s[i] = i = set_find(s, s[i])
	return i
def set_union(s, i, j):
	i = set_find(s, i)
	j = set_find(s, j)
	if i != j:
		if s[i] == None:
			s[i] = j
		elif s[j] == None:
			s[j] = i
		elif s[i] != s[j]:
			return False
	return True



def match(line1, line2):
	if len(line1) != len(line2):
		return '-'
	patterns1 = {}
	patterns2 = {}
	s = [None] * (len(line1) * 2)
	for i in range(len(line1)):
		w1 = line1[i]
		w2 = line2[i]
		if w1[0] == '<':
			if not set_union(s, i * 2, patterns1.setdefault(w1[1:-1], i * 2)):
				return '-'
		else:
			s[i * 2] = w1
		if w2[0] == '<':
			if not set_union(s, i * 2 + 1, patterns2.setdefault(w2[1:-1], i * 2 + 1)):
				return '-'
		else:
			s[i * 2 + 1] = w2
		if not set_union(s, i * 2, i * 2 + 1):
			return '-'
	return ' '.join([str(s[set_find(s, i * 2)]).lower() for i in range(len(line1))])

N = int(input())
for n in range(N):
	line1 = input().split()
	line2 = input().split()
	print(match(line1, line2))
