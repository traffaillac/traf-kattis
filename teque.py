# same as collections.deque, but with O(1) random access
class deque:
	def __init__(self, buf=None, start=0, end=0):
		self.buf = buf if buf else [None] * 1000001
		self.start = start
		self.end = end
	def __len__(self):
		b, s, e = self.buf, self.start, self.end
		return e - s if e >= s else e + len(b) - s
	def __getitem__(self, i):
		return self.buf[self._shift(i)]
	def __setitem__(self, i, v):
		self.buf[self._shift(i)] = v
	def __repr__(self):
		return "[" + ", ".join(map(repr, self)) + "]"
	
	def append(self, x):
		b, s, e = self.buf, self.start, self.end
		b[e] = x
		self.end = e = e+1 if e+1<len(b) else 0
		self._tail(b, s, e)
	def appendleft(self, x):
		b, s, e = self.buf, self.start, self.end
		self.start = s = s-1 if s>0 else len(b)-1
		b[s] = x
		self._tail(b, s, e)
	def pop(self):
		b, s, e = self.buf, self.start, self.end
		self.end = e = e-1 if e>0 else len(b)-1
		v, b[e] = b[e], None
		return v
	def popleft(self):
		b, s, e = self.buf, self.start, self.end
		v, b[s] = b[s], None
		self.start = s+1 if s+1<len(b) else 0
		return v
	
	def _shift(self, i):
		b, s, e = self.buf, self.start, self.end
		if not -len(self) <= i < len(self):
			raise IndexError
		if i >= 0:
			return s+i if s+i<len(b) else i-len(b)+s
		else:
			return e+i if e+i>=0 else i+e+len(b)
	def _tail(self, b, s, e):
		if s == e:
			self.buf = b[:s] + [None]*len(b) + b[s:]
			self.start = s + len(b)

from sys import stdin

left = deque()
right = deque()
for _ in range(int(stdin.readline())):
	op, i = stdin.readline().split()
	i = int(i)
	if op == "push_back":
		right.append(i)
	elif op == "push_front":
		left.appendleft(i)
	elif op == "push_middle":
		left.append(i)
	else:
		print(left[i] if i < len(left) else right[i - len(left)])
	# ensure that len(left)==len(right) or len(left)==len(right)+1
	if len(left) < len(right):
		left.append(right.popleft())
	elif len(left) > len(right) + 1:
		right.appendleft(left.pop())
