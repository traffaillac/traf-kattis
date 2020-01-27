while True:
	a, b = input().split()
	if a == '0' and b == '0':
		break
	carries = 0
	carry = 0
	for i in range(max(len(a), len(b))):
		carry = ((int(a[-i - 1]) if i < len(a) else 0) + (int(b[-i - 1]) if i < len(b) else 0) + carry) // 10
		carries += carry
	print('No carry operation.' if carries == 0 else
		'1 carry operation.' if carries == 1 else
		str(carries) + ' carry operations.')
