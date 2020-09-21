_, code, guess = input().split()
histc, histg = [0] * 26, [0] * 26
r, s = 0, 0
for c, g in zip(code, guess):
	if c == g:
		r += 1
	else:
		histc[ord(c) - 65] += 1
		histg[ord(g) - 65] += 1
print(r, sum(min(histc[i], histg[i]) for i in range(26)))
