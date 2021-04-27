while True:
	n = int(input())-1
	if n < 0:
		break
	S = [str(3**i) for i in range(n.bit_length()) if n&1<<i]
	print("{ "+", ".join(S)+" }" if S else "{ }")
