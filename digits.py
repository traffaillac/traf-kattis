# worst is 1000000 digits->1_000_000->7->1->1
while True:
	x = input()
	if x == 'END': break
	print(1 if x=='1' else 2 if len(x)==1 else 3 if len(x)<10 else 4)
