class Window:
	def __init__(self, x, y, X, Y):
		self.x = x
		self.y = y
		self.X = X
		self.Y = Y
	def __repr__(self):
		return f'{self.x} {self.y} {self.X-self.x} {self.Y-self.y}'
	def intersects(self, x, y, X, Y):
		return self.x<X and self.X>x and self.y<Y and self.Y>y


xmax, ymax = (int(i) for i in input().split())
windows = [] # x1,y1,x2,y2
for i in range(1, 257):
	try:
		cmd, *args = input().split()
	except: break
	x, y = int(args[0]), int(args[1])
	w = None
	
	if cmd == 'CLOSE' or cmd == 'RESIZE' or cmd == 'MOVE':
		try:
			w = next(w for w in windows if w.x<=x<w.X and w.y<=y<w.Y)
			x, y = w.x, w.y
		except:
			print(f'Command {i}: {cmd} - no window at given position')
			continue
	
	if cmd == 'OPEN' or cmd == 'RESIZE':
		X, Y = x+int(args[2]), y+int(args[3])
		if X>xmax or Y>ymax or any(v!=w and v.intersects(x, y, X, Y) for v in windows):
			print(f'Command {i}: {cmd} - window does not fit')
			continue
	
	if cmd == 'OPEN':
		windows.append(Window(x, y, X, Y))
	elif cmd == 'CLOSE':
		windows.remove(w)
	elif cmd == 'RESIZE':
		w.X, w.Y = X, Y
	elif cmd == 'MOVE':
		dx, dy = int(args[2]), int(args[3])
		moving = {w}
		
		while dx > 0:
			move, bump = dx, None
			for w in windows:
				if w in moving: continue
				for m in moving:
					if 0<=w.x-m.X<move and w.Y>m.y and m.Y>w.y:
						move, bump = w.x-m.X, w
			X = max(m.X for m in moving)
			if X+move > xmax:
				print(f'Command {i}: {cmd} - moved {int(args[2])-(X+dx-xmax)} instead of {args[2]}')
				move = dx = xmax-X
			for m in moving:
				m.x += move
				m.X += move
			moving.add(bump)
			dx -= move
		
		while dx < 0:
			move, bump = dx, None
			for w in windows:
				if w in moving: continue
				for m in moving:
					if move<w.X-m.x<=0 and w.Y>m.y and m.Y>w.y:
						move, bump = w.X-m.x, w
			X = min(m.x for m in moving)
			if X+move < 0:
				print(f'Command {i}: {cmd} - moved {-int(args[2])+X+dx} instead of {-int(args[2])}')
				move = dx = -X
			for m in moving:
				m.x += move
				m.X += move
			moving.add(bump)
			dx -= move
		
		while dy > 0:
			move, bump = dy, None
			for w in windows:
				if w in moving: continue
				for m in moving:
					if 0<=w.y-m.Y<move and w.X>m.x and m.X>w.x:
						move, bump = w.y-m.Y, w
			Y = max(m.Y for m in moving)
			if Y+move > ymax:
				print(f'Command {i}: {cmd} - moved {int(args[3])-(Y+dy-ymax)} instead of {args[3]}')
				move = dy = ymax-Y
			for m in moving:
				m.y += move
				m.Y += move
			moving.add(bump)
			dy -= move
		
		while dy < 0:
			move, bump = dy, None
			for w in windows:
				if w in moving: continue
				for m in moving:
					if move<w.Y-m.y<=0 and w.X>m.x and m.X>w.x:
						move, bump = w.Y-m.y, w
			Y = min(m.y for m in moving)
			if Y+move < 0:
				print(f'Command {i}: {cmd} - moved {-int(args[3])+Y+dy} instead of {-int(args[3])}')
				move = dy = -Y
			for m in moving:
				m.y += move
				m.Y += move
			moving.add(bump)
			dy -= move

print(f'{len(windows)} window(s):')
for w in windows:
	print(w)
