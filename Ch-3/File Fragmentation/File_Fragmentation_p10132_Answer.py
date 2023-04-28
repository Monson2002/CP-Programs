import sys

def right(x):
	return x
	#return min(x,x[::-1])

lines = iter(sys.stdin.read().splitlines())

T = int(next(lines))
next(lines)

out = []

for i in range(T):
	
	frags = []
	cont = 0
	
	j = 0
	for line in lines:
		num = line.split()
		if len(num) == 0:
			if line == "":
				break
		else:
			if j < 288:
				cont += len(line.split()[0])
				frags.append(line.split()[0])
			j += 1
	
	lon = cont//(j//2)	
	grps = [None]*(-1+lon)
	
	for frag in frags:
		if grps[len(frag)-1] == None:
			grps[len(frag)-1] = set()
		grps[len(frag)-1].add(right(frag))
	
	r = set()
	
	bu = False
	first = True
	
	for n,grp in sorted([x for x in enumerate(grps) if x[1] != None and x[0] < lon//2 ], key = lambda x:len(x[1])):
		for frag in grp:
			l = []
			for comp in grps[lon-2-n]:
				l.append(right(frag+comp))
				#l.append(right(frag+comp[::-1]))
				#l.append(right(frag[::-1]+comp))
				l.append(right(comp+frag))
			
			if first:
				first = False
				r.update(l)
			else:
				r.intersection_update(l)	
			if len(r) == 1:
				bu = True
				break
			
		if bu:
			break
	
	out.append(sorted(list(r))[0]+"\n")

print("\n".join(out),sep="",end="")