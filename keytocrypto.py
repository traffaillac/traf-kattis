C = [ord(c)-65 for c in input()]
K = [ord(c)-65 for c in input()]
n = len(K)
for i, c in enumerate(C):
	K.append((c-K[i])%26)
print(''.join(chr(65+k) for k in K[n:]))