from string import ascii_letters, digits

S = input()
secret = []
for word in S.split():
	if set(word).intersection(ascii_letters+digits) <= {'u', 'm'}:
		for c in word:
			if c == 'u':
				secret.append('1')
			elif c == 'm':
				secret.append('0')
secret = ''.join(secret)
for i in range(0, len(secret), 7):
	print(chr(int(secret[i:i+7], 2)), end='')
print()
