from sys import stdin

morse = {'A':'.-', 'H':'....', 'O':'---', 'V':'...-', 'B':'-...', 'I':'..', 'P':'.--.', 'W':'.--', 'C':'-.-.', 'J':'.---', 'Q':'--.-', 'X':'-..-', 'D':'-..', 'K':'-.-', 'R':'.-.', 'Y':'-.--', 'E':'.', 'L':'.-..', 'S':'...', 'Z':'--..', 'F':'..-.', 'M':'--', 'T':'-', 'G':'--.', 'N':'-.', 'U':'..-', '_':'..--', '.':'---.', ',':'.-.-', '?':'----'}
inverse = {l:m for m,l in morse.items()}

for line in stdin:
	code = []
	lengths = []
	for c in line.strip():
		code.extend(morse[c])
		lengths.append(len(morse[c]))
	lengths.reverse()
	i = 0
	for l in lengths:
		print(inverse[''.join(code[i:i+l])], end='')
		i += l
	print()
