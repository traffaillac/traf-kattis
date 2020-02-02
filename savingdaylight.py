while True:
	try: month,day,year,dawn,dusk = input().split()
	except: break
	h0,m0 = (int(i) for i in dawn.split(':'))
	h1,m1 = (int(i) for i in dusk.split(':'))
	m = (h1-h0)*60+m1-m0
	print(month, day, year, m//60, "hours", m%60, "minutes")