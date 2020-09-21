from collections import Counter
from statistics import median_low, median_high

N, t = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
C = Counter(A)
if t == 1:
	print("Yes" if any(7777-x in C for x in C) else "No")
elif t == 2:
	print("Unique" if len(A)==len(C) else "Contains duplicate")
elif t == 3:
	print(next((a for a, c in C.items() if c > N//2), -1))
elif t == 4:
	print(median_low(A) if N%2==1 else f"{median_low(A)} {median_high(A)}")
elif t == 5:
	print(*sorted(a for a in A if 100<=a<=999))
