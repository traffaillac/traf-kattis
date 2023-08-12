D = {}
for h in range(12):
	for m in range(60):
		D[(m*60-(h*60+m)*5)%3600] = f"{h:02d}:{m:02d}"
print(D[int(input())])