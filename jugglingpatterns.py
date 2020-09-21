from sys import stdin

for p in stdin.read().split():
	if sum(map(int, p)) % len(p) > 0:
		print(f"{p}: invalid # of balls")
		continue
	catches = [0] * (len(p)+18)
	for beat in range(len(p)+9):
		catch = catches[beat]
		throw = int(p[beat % len(p)])
		if catch > (throw > 0):
			print(f"{p}: invalid pattern")
			break
		catches[beat + throw] += 1
	else:
		print(f"{p}: valid with {sum(map(int, p))//len(p)} balls")
