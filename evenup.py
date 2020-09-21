n = int(input())
rem, parity = 0, 0
for card in map(int, input().split()):
	if rem == 0 or card % 2 != parity:
		rem += 1
		parity = card % 2
	else:
		rem -= 1
		parity = 1 - parity
print(rem)
