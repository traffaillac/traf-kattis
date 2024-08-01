for _ in range(int(input())):
	C, D, H, M = input().split()
	M = int(H)*60+int(M)+(int(D) if C=='F' else -int(D))
	print(M//60%24, M%60)