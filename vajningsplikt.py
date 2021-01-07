N, S, E, W = 'North', 'South', 'East', 'West'
a, b, c = input().split()
print('Yes' if (a, b, c) in (
	(S, N, E), (E, W, N), (N, S, W), (W, E, S), # straight through
	(S, W, E), (E, S, N), (N, E, W), (W, N, S), # left vs right
	(S, W, N), (E, S, W), (N, E, S), (W, N, E)) # left vs front
	else 'No')
