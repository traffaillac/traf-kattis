# find d such that (e+d)%365 == (m+d)%687 == 0
from sys import stdin
for t, l in enumerate(stdin):
	e, m = map(int, l.split())
	print(f"Case {t+1}:", next(x for x in range(999999) if (e+x)%365==(m+x)%687==0))