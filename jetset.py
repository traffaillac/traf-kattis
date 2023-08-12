def flight(prev, lon, visited):
	if lon == (prev + 180) % 360:
		for l in range(720): # the flight goes through a pole
			visited[l] = True
	elif lon-prev < -180:
		for l in range(0, lon*2+1):
			visited[l] = True
		for l in range(prev*2, 720):
			visited[l] = True
	elif -180 < lon-prev < 0:
		for l in range(lon*2, prev*2+1):
			visited[l] = True
	elif 0 < lon-prev < 180:
		for l in range(prev*2, lon*2+1):
			visited[l] = True
	elif 180 < lon-prev:
		for l in range(0, prev*2+1):
			visited[l] = True
		for l in range(lon*2, 720):
			visited[l] = True

def main():
	n = int(input())
	visited = [False] * 720
	start = int(input().split()[1]) + 180
	prev = start
	for _ in range(n-1):
		lon = int(input().split()[1]) + 180
		flight(prev, lon, visited)
		prev = lon
	flight(prev, start, visited)
	print("yes" if all(visited) else "no %.1f"%(visited.index(False)/2-180,))

main()
