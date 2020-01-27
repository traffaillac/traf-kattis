for t in range(int(input())):
	votes = [int(input()) for n in range(int(input()))]
	w = max(range(len(votes)), key=votes.__getitem__)
	print('no winner' if votes.count(votes[w])>1 else
		f'majority winner {w+1}' if votes[w]>sum(votes)//2 else
		f'minority winner {w+1}')
