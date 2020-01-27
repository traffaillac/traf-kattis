N = int(input())
b = input()
while N > 2:
	print(f'{N} bottles of {b} on the wall, {N} bottles of {b}.')
	N -= 1
	print(f'Take one down, pass it around, {N} bottles of {b} on the wall.')
	print()
if N == 2:
	print(f'2 bottles of {b} on the wall, 2 bottles of {b}.')
	print(f'Take one down, pass it around, 1 bottle of {b} on the wall.')
	print()
print(f'1 bottle of {b} on the wall, 1 bottle of {b}.')
print(f'Take it down, pass it around, no more bottles of {b}.')
