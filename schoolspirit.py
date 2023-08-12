def score(S):
	return sum(s*.8**i for i, s in enumerate(S))/5
n = int(input())
S = [int(input()) for _ in range(n)]
print(score(S))
print(sum(score(S[:i]+S[i+1:]) for i in range(n))/n)