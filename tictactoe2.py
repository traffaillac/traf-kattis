# mauvais nombre de X ou O
# gagnant incohérent avec le nombre de X ou O
# gagnants simultanés
# un gagnant par lignes parallèles
def win(g, c):
	return (g[0]==g[1]==g[2]==c or g[3]==g[4]==g[5]==c or g[6]==g[7]==g[8]==c or
		g[0]==g[3]==g[6]==c or g[1]==g[4]==g[7]==c or g[2]==g[5]==g[8]==c or
		g[0]==g[4]==g[8]==c or g[2]==g[4]==g[6]==c)

while True:
	try: input()
	except: break
	g = input()+input()+input()
	x,o,wx,wo = g.count('X'),g.count('O'),win(g,'X'),win(g,'O')
	print('no' if not o<=x<=o+1 or wx and x!=o+1 or wo and o!=x or wx and wo else 'yes')
