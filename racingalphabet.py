from math import pi
from string import ascii_uppercase
T = ascii_uppercase + " '"
U = pi*60/28/15
for _ in range(int(input())):
	s, t = list(map(T.index, input())), 0
	for a, b in zip(s, s[1:]):
		t += min((a-b)%28, (b-a)%28) * U
	print(t+len(s))
