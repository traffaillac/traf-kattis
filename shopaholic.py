input()
prices = [int(p) for p in input().split()]
prices.sort(reverse=True)
print(sum(prices[i+2] for i in range(0, len(prices)-2, 3)))
	