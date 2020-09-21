# WA on test 3/4

from bisect import bisect_left
from sys import stdin, stdout

variables = [0] * 26
statements = []
for stm in stdin:
	label, command, data = stm.rstrip().split(maxsplit=2)
	statements.append((int(label), command, data))
statements.sort()
ip = 0
while ip < len(statements):
	_, command, data = statements[ip]
	if command == "LET":
		x, eq, *exp = data.split()
		assert eq == "="
		y = variables[ord(exp[0])-65] if exp[0].isupper() else int(exp[0])
		z = variables[ord(exp[-1])-65] if exp[-1].isupper() else int(exp[-1])
		if len(exp) == 1:
			variables[ord(x)-65] = y
		elif exp[1] == "+":
			variables[ord(x)-65] = (y + z + 2**31) % 2**32 - 2**31
		elif exp[1] == "-":
			variables[ord(x)-65] = (y - z + 2**31) % 2**32 - 2**31
		elif exp[1] == "*":
			variables[ord(x)-65] = (y * z + 2**31) % 2**32 - 2**31
		else:
			assert len(exp) == 3 and exp[1] == "/"
			variables[ord(x)-65] = y//z if y*z>0 else -y//z
	elif command == "IF":
		x, op, y, then, goto, l = data.split()
		assert then == "THEN" and goto == "GOTO"
		x = variables[ord(x)-65] if x.isupper() else int(x)
		y = variables[ord(y)-65] if y.isupper() else int(y)
		assert op == "=" or op == "<>" or op == ">" or op == "<" or op == "<=" or op == ">="
		if (op == "=" and x == y or op == "<>" and x != y or
		    op == ">" and x > y or op == "<" and x < y or
		    op == "<=" and x <= y or op == ">=" and x >= y):
			ip = bisect_left(statements, (int(l),)) - 1
	elif command == "PRINT":
		stdout.write(data[1:-1] if data[0]=="\"" else str(variables[ord(data)-65]))
	else:
		assert command == "PRINTLN"
		print(data[1:-1] if data[0]=="\"" else variables[ord(data)-65])
	ip += 1
