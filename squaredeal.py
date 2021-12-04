def test(H0, W0, H1, W1, H2, W2, i):
	if i & 1:
		H0, W0 = W0, H0
	if i & 2:
		H1, W1 = W1, H1
	if i & 4:
		H2, W2 = W2, H2
	return W0 == W1 == W2 == H0+H1+H2 or \
	       W0+W1 == W0+W2 == H0 == H1+H2 or \
	       W0+W1 == W1+W2 == H1 == H0+H2 or \
	       W0+W2 == W1+W2 == H2 == H0+H1

H0, W0 = map(int, input().split())
H1, W1 = map(int, input().split())
H2, W2 = map(int, input().split())
print('YES' if any(test(H0, W0, H1, W1, H2, W2, i) for i in range(8)) else 'NO')
