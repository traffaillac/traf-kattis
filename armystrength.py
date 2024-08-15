for _ in range(int(input())):
	input()
	input()
	g = max(map(int, input().split()))
	m = max(map(int, input().split()))
	print("Godzilla" if g>=m else "MechaGodzilla")