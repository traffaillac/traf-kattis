C, K = map(int, input().split())
bill = 10 ** K
print((C + bill // 2) // bill * bill)
