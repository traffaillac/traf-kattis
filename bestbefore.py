def date(year:int, month:int, day:int):
	if year <= 99:
		year += 2000
	elif year <= 1999:
		return "None"
	if not 1<=month<=12:
		return "None"
	days = (31,29 if year%4==0 and (year%100>0 or year%400==0) else 28,31,30,31,30,31,31,30,31,30,31)
	if not 1<=day<=days[month-1]:
		return "None"
	return f"{year}-{month:02}-{day:02}"

s = input()
A,B,C = (int(i) for i in s.split('/'))
res = min(date(A,B,C), date(A,C,B), date(B,A,C), date(B,C,A), date(C,A,B), date(C,B,A))
print(res if res!="None" else f"{s} is illegal")