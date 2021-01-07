try:
	while True:
		n = int(input())
		s = input()
		for _ in range(n):
			s = ''.join('\\'+c if ord('!')<=ord(c)<=ord('*') or ord('[')<=ord(c)<=ord(']') else c for c in s)
		print(s)
except:
	pass
