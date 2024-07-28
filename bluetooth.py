S = [8, 8, 8, 8]
for _ in range(int(input())):
	t, s = input().split()
	S[0 if t[1]=='+' else 1 if t[0]=='+' else 2 if t[1]=='-' else 3] -= 1 if s=='m' else 8
print(0 if S[1]>0<S[3] else 1 if S[0]>0<S[2] else 2)