from heapq import heappush, heappop

for _ in range(int(input())):
	sell = []
	buy = []
	stock = "-"
	for _ in range(int(input())):
		order, x, _, _, y = input().split()
		x, y = int(x), int(y)
		if order == "sell":
			heappush(sell, (y, x))
		else:
			heappush(buy, (-y, x))
		while sell and buy and sell[0][0] <= -buy[0][0]:
			ps, ns = heappop(sell)
			pb, nb = heappop(buy)
			stock = ps
			if ns > nb:
				heappush(sell, (ps, ns-nb))
			if ns < nb:
				heappush(buy, (pb, nb-ns))
		print(sell[0][0] if sell else "-", -buy[0][0] if buy else "-", stock)
