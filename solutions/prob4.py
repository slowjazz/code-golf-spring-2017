f = open("4.txt","r")
o = open("4out.txt","w")
x =[float(p.split(' ')[0]) for p in f] 
f.seek(0)
y =[]
for p in f:
	y.append(float(p.split(' ')[-1][:-1]))
mx = sum(x)/(len(x)) 
my = sum(y)/(len(y))
xx = [e-mx for e in x]
b = [a-my for a in y]
xy = [a*b for a,b in zip(xx,b)]
m = sum(xy)/sum([a**2 for a in xx])
i = my - m*mx
o.write(str(round(i/m,3)))
o.close()