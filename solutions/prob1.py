f = open("1.txt","r")
out = open("1out.txt","w")
for l in f:
	l = int(l)
	c =0
	for t in range(2,l+1):
		p = True
		for x in range(2,t):
			if t%x==0: p= False
		if p: c+=1
	out.write(str(c)+"\n")
out.close()