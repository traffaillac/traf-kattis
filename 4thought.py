from itertools import product

for _ in range(int(input())):
	n = int(input())
	for a, b, c in product(['*', '+', '-', '//'], repeat=3):
		expr = '4 ' + a + ' 4 ' + b + ' 4 ' + c + ' 4'
		if eval(expr) == n:
			print(expr.replace('//', '/'), '=', n)
			break
	else:
		print('no solution')
