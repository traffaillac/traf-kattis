N = int(input())
grid = [input() for _ in range(N)]
houses = [(r, c) for r in range(N) for c in range(N) if grid[r][c]=='H']
spies = [(r, c) for r in range(N) for c in range(N) if grid[r][c]=='S']
print(max(min(abs(rs-rh)+abs(cs-ch) for rh, ch in houses) for rs, cs in spies))
