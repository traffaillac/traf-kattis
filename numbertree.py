from itertools import accumulate

H, *path = input().split()
H, path = int(H), path[0] if path else ""
col = int(path.replace("L", "1").replace("R", "0"), 2) if path else 0
rows = [1]
for i in range(H, 0, -1):
	rows.append(rows[-1] + 2**i)
print(rows[H-len(path)] + col)
