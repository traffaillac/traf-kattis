# 1110?
# 00011
for c in range(int(input())):
	S = input()
	T = input()
	sets = sum(1 for s,t in zip(S,T) if s=='0' and t=='1')
	unsets = sum(1 for s,t in zip(S,T) if s=='1' and t=='0')
	to0 = sum(1 for s,t in zip(S,T) if s=='?' and t=='0')
	to1 = sum(1 for s,t in zip(S,T) if s=='?' and t=='1')
	moves = -1 if unsets>sets+to1 else unsets+max(sets-unsets,0)+to0+to1
	print(f'Case {c+1}: {moves}')
