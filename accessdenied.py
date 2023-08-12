from string import ascii_uppercase, ascii_lowercase, digits

letters = ascii_uppercase + ascii_lowercase + digits
guess = [letters[0]]
while True:
	print("".join(guess), flush=True)
	response = input()
	if response == "ACCESS GRANTED":
		break
	t = int(response[15:].split()[0])
	if t == 5:
		guess.append(letters[0])
	else:
		i = (t-14) // 9
		guess[i] = letters[letters.index(guess[i])+1]
