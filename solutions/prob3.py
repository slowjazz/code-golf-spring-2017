f = open("3.txt","r")
o = open("3out.txt","w")
d = [l[:-1] for l in f]
b =[True for i in range(len(d))]
for x in d:
	for y in d:
		if (x in y or y in x) and x!=y:
			b[d.index(x)] = b[d.index(y)] = False
for a in range(len(b)):
	if b[a]:o.write(d[a]+"\n")
o.close

	