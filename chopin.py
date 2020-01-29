alt = {
	'Ab minor': 'G# minor',
	'D# major': 'Eb major',
	'A# major': 'Bb major',
	'D# minor': 'Eb minor',
	'A# minor': 'Bb minor',
	'Gb major': 'F# major',
	'C# major': 'Db major',
	'Gb minor': 'F# minor',
	'Db minor': 'C# minor',
	'G# major': 'Ab major',
	'G# minor': 'Ab minor',
	'Eb major': 'D# major',
	'Bb major': 'A# major',
	'Eb minor': 'D# minor',
	'Bb minor': 'A# minor',
	'F# major': 'Gb major',
	'Db major': 'C# major',
	'F# minor': 'Gb minor',
	'C# minor': 'Db minor',
	'Ab major': 'G# major'}
for i in range(1, 6):
	try: name = input()
	except: break
	print(f'Case {i}: {alt.get(name, "UNIQUE")}')
