end0 = [1] * 10000 # number of strings that end with 0
end1 = [1] * 10000 # number of strings that end with 1
for n in range(1, 10000):
	end0[n] = (end0[n-1] + end1[n-1]) % 1_000_000_007
	end1[n] = end0[n-1]
for _ in range(int(input())):
	n = int(input())-1
	print((end0[n] + end1[n]) % 1_000_000_007)
