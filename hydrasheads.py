while 1:
	H,T=map(int,input().split())
	if H==T==0:break
	H+=T//2+T%2;print(-1 if T==~H&1==0 else(H+1)//2+T//2+T%2*2+H%2*3)