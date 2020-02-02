# Longest gap inbetween years
# Chosen date the day before 1st January
from itertools import accumulate
from bisect import bisect

days = [0]+list(accumulate((31,28,31,30,31,30,31,31,30,31,30,31)))
birthdays = []
n = int(input())
for _ in range(n):
	m,d = (int(i) for i in input().split()[1].split('-'))
	birthdays.append(days[m-1]+d-1)
birthdays.sort()
# gap size, days until next 27th October
gaps = [((birthdays[i]-birthdays[(i-1)%n])%365, (days[9]+26-birthdays[i]+1)%365) for i in range(n)]
chosen = (days[9]+26-max(gaps)[1])%365
month = bisect(days, chosen)
print(f"{month:02}-{chosen-days[month-1]+1:02}")
