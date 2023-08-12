O = "abcdefghijklmnopqrstuvwxyz"
N = ["@","8","(","|)","3","#","6","[-]","|","_|","|<","1","[]\\/[]","[]\\[]","0","|D","(,)","|Z","$","']['","|_|","\\/","\\/\\/","}{","`/","2"]
s = input().lower()
for o, n in zip(O, N):
	s = s.replace(o, n)
print(s)