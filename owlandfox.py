def main():
	for _ in range(int(input())):
		N = list(map(int, input()))
		i = len(N)-1
		while N[i] == 0:
			i -= 1
		N[i] -= 1
		print(int(''.join(map(str, N))))
main()