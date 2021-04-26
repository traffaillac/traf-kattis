last = 0
rounds = 1
for _ in range(int(input())):
	clerk = int(input())
	rounds += clerk < last
	last = clerk
print(rounds)
