# my-first-task
**Introduction**
To intersect .vcf and .Bed and print the output in vcf format.


**Prerequisites**

Before you continue, ensure you have met the following requirements:

* You have installed the latest version of python.
* You are using a Linux machine.

**Installation**
pandas and argparse are easiest to use when installed with pip

pip install pandas
pip install argparse

**Usage**
To use pandas and argparse we need to import them.

import pandas as pd
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument("--input1", help = "vcf file")

# Parse the argument
args = parser.parse_args()

**Create outfile.vcf in write mode**

outF = open("myOutFile.vcf", "w")


**open user-input file and save in filehandle**

f1 = open(args.input1)
f2 = open(args.input2)

**read user-input .vcf file using pandas and skip headers with skiprows**
**pd.read_csv(filehandle, separator, skiprows=number of rows to skip, #usecols=number of columns to be user if no headers available)**

data1 = pd.read_csv(f1, sep ='\t', skiprows=22)

#read .BED file

data2 = pd.read_csv(f2, sep ='\t', header = None, usecols = [0,1,2])


# converting column data from .BED to list
bchrom = data2[0].tolist()

# converting column data from .vcf to list

vchrom = data1["#CHROM"].tolist()
vpos = data1["POS"].tolist()


**converting row data from .vcf to list**

dfrows = data1.to_numpy().tolist()


for i in range(len(vpos)):
	for j in range(len(bstart)):
		if ((vpos[i] >= bstart[j]) and (vpos[i]<= bend[j])):
			#print(dfrows[i])
			outF.write(str(dfrows[i]))
			outF.write("\n")
			#print (bchrom[j],"\t",bstart[j], "\t", bend[j], "\t", vchrom[i],"\t",vpos[i])
