n, m = map(int, input().split())
cost = 0
# as long as it is possible to upgrade m-1 roads among n-1 cities, link a city with only 1 pricey road
while m>0 and m-1 <= (n-1)*(n-2)//2:
	cost += m
	m -= 1
	n -= 1
label = 1
for i in range(n-1):
	label += i
	cost += label
print(cost)
