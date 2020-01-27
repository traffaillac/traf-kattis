penalties = {}
solved = set()
time = 0
while True:
	try:
		m, pb, res = input().split()
	except: break
	if pb in solved: continue
	if res == 'right':
		time += penalties.get(pb, 0) + int(m)
		solved.add(pb)
	else:
		penalties[pb] = penalties.get(pb, 0) + 20
print(len(solved), time)
