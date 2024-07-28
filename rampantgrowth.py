r, c = map(int, input().split())
print(r * pow(r-1, c-1, 998244353) % 998244353)