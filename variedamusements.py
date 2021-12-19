def main():
	n, a, b, c = map(int, input().split())
	A, B, C = a, b, c # number of sequences ending with a ride of type x
	P = 1_000_000_007
	for _ in range(n-1):
		A, B, C = (B+C)*a%P, (A+C)*b%P, (A+B)*c%P
	print((A+B+C)%P)

main()
