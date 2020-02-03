timezones = {"UTC":0, "GMT":0, "BST":60, "IST":60, "WET":0, "WEST":60, "CET":60, "CEST":120, "EET":120, "EEST":180, "MSK":180, "MSD":240, "AST":-240, "ADT":-180, "NST":-210, "NDT":-150, "EST":-300, "EDT":-240, "CST":-360, "CDT":-300, "MST":-420, "MDT":-360, "PST":-480, "PDT":-420, "HST":-600, "AKST":-540, "AKDT":-480, "AEST":600, "AEDT":660, "ACST":570, "ACDT":630, "AWST":480}
for _ in range(int(input())):
	*time, src, dst = input().split()
	if time[0] == "midnight":
		time = 0
	elif time[0] == "noon":
		time = 720
	else:
		h,m = (int(i) for i in time[0].split(':'))
		time = h%12*60+m if time[1]=="a.m." else h%12*60+m+720
	time = (time - timezones[src] + timezones[dst]) % 1440
	if time == 0:
		print("midnight")
	elif time == 720:
		print("noon")
	else:
		print(f"{(time//60-1)%12+1}:{time%60:02} {'a.m.' if time<720 else 'p.m.'}")
