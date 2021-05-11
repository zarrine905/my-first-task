#To intersect .vcf with .bed without using pandas 
#11/05/21

f1 = open("WithoutpandasResult.vcf", "w")

#To read columns of vcf into list
f = open("example.vcf","r")
lines = f.readlines()
#print(lines[0])
vpos = []
rowlist = []
header = ""
for vline in lines:
	if ("#" in vline):
		header += vline + "\n"
	elif ("#" not in vline):
		#vpos.append(vline)
		#print (line)
		vline = vline.split()	#To read columns of vcf 
		vpos.append(vline[1])
		rowlist.append(vline)   #To read lines/rows of vcf into list

#print(header)
f1.write(header)
#print(vpos)
#print(rowlist[0])


#To read columns of .bed into list
fh = open("example.bed", "r")
blines = fh.readlines()
#print(blines)

bstart=[]
bend =[]
for bline in blines:
	bline = bline.split()
	#print(bline[2])
	bstart.append(bline[1])
	bend.append(bline[2])
#print(bstart)
#print(bend)



for i in range(len(vpos)):
	for j in range(len(bstart)):
		if ((vpos[i] >= bstart[j]) and (vpos[i]<= bend[j])):
			list_val = rowlist[i]
			myjoin = "\t".join(map(str, list_val))
			#print(myjoin)
			f1.write(myjoin+"\n")
			
		




