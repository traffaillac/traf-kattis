months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i in range(int(input())):
	d, m = input().split()
	day = months.index(m) * 31 + int(d)
	print(
		'Aquarius' if 0*31+21<=day<=1*31+19 else
		'Pisces' if 1*31+20<=day<=2*31+20 else
		'Aries' if 2*31+21<=day<=3*31+20 else
		'Taurus' if 3*31+21<=day<=4*31+20 else
		'Gemini' if 4*31+21<=day<=5*31+21 else
		'Cancer' if 5*31+22<=day<=6*31+22 else
		'Leo' if 6*31+23<=day<=7*31+22 else
		'Virgo' if 7*31+23<=day<=8*31+21 else
		'Libra' if 8*31+22<=day<=9*31+22 else
		'Scorpio' if 9*31+23<=day<=10*31+22 else
		'Sagittarius' if 10*31+23<=day<=11*31+21 else
		'Capricorn')
