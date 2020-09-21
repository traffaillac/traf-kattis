AND = {"??": "?", "?1": "?", "?0": "0",
	"1?": "?", "11": "1", "10": "0",
	"0?": "0", "01": "0", "00": "0"}
OR = {"??": "?", "?1": "1", "?0": "?",
	"1?": "1", "11": "1", "10": "1",
	"0?": "?", "01": "1", "00": "0"}
while True:
	n = int(input())
	if n == 0: break
	bits = ["?"] * 32
	for _ in range(n):
		inst, i, *j = input().split()
		if inst == "CLEAR":
			bits[31-int(i)] = "0"
		elif inst == "SET":
			bits[31-int(i)] = "1"
		elif inst == "OR":
			bits[31-int(i)] = OR[bits[31-int(i)]+bits[31-int(j[0])]]
		elif inst == "AND":
			bits[31-int(i)] = AND[bits[31-int(i)]+bits[31-int(j[0])]]
	print("".join(bits))
