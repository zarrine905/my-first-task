import pandas as pd




f = open("withoutpandasResult.vcf", "w")


#To read lines/rows of vcf into list
rowlist=[]
header=[]
for line in open("example.vcf"):
    li=line.strip()
    if li.startswith("#"):
        header.append(line)
#print(str(header))
#print(' '.join(header))
#f.write(' '.join(header))
print(*header, sep = "\n") 


#To read lines/rows of vcf into list
rowlist=[]
header=[]
for line in open("example.vcf"):
    li=line.strip()
    if not li.startswith("#"):
        rowlist.append(line)
 
#print(rowlist[0])



#To read columns of vcf into list
f = open("example.bed","r")
lines = f.readlines()
#print(lines[0])
vpos =[]
for vline in lines:
	if not vline.startswith("#"):
		#print (line)
		vline = vline.split()
		vpos.append(vline[1])
#print(len(vpos))
	

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
			print(rowlist[i])
			#f.write(str(rowlist[i]))
			
		



