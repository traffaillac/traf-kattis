dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
notdominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
N, B = input().split()
points = 0
for _ in range(4*int(N)):
	num, suit = input()
	points += dominant[num] if suit==B else notdominant[num]
print(points)