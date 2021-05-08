#Script to intersect .vcf with .BED file
#Author: Zarrine Raazi
#03/05/2021

import pandas as pd
import argparse


# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument("--input1", help = "vcf file")
parser.add_argument("--input2", help = "bed file")
#parser.add_argument("--output", help = "vcf outfile ")
# Parse the argument
args = parser.parse_args()


#print('VCF file:', args.input1)
#print('BED file:', args.input2)
#print('OUT:', args.output)


outF = open("myOutFile.vcf", "w")

f1 = open(args.input1)
#read .vcf file
data1 = pd.read_csv(f1, sep ='\t', skiprows = 22)
#print(data1)

#reading rows into list
dfrows = data1.to_numpy().tolist()

#print(dfrows)


# converting column data to list
vchrom = data1["#CHROM"].tolist()
vpos = data1["POS"].tolist()


f2 = open(args.input2)

#read .BED file
data2 = pd.read_csv(f2, sep ='\t', header = None, usecols = [0,1,2])

# converting column data to list
bchrom = data2[0].tolist()
bstart = data2[1].tolist()
bend = data2[2].tolist()



for i in range(len(vpos)):
	for j in range(len(bstart)):
		if ((vpos[i] >= bstart[j]) and (vpos[i]<= bend[j])):
			#print(dfrows[i])
			#outF.write(str(dfrows[i]))
			#outF.write("\n")
			#print (bchrom[j],"\t",bstart[j], "\t", bend[j], "\t", vchrom[i],"\t",vpos[i])
			list_val = dfrows[i]
			outF.write(", ".join(map(str, list_val)))
			outF.write("\n")
			
			



    
    
