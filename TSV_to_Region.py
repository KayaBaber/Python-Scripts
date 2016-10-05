import sys
import math


#first argument is input
#second argument is output
inputTSV = sys.argv[1]
#outputRegion = str(sys.argv[2])

#Reads TSV to a nested list
with open(inputTSV) as input:
    TSVlist = zip(*(line.strip().split('\t') for line in input))


startLine = 11
#seperates TSV into several lists for each property of the regions
NAMElist = TSVlist[2][startLine:]
RAlist = TSVlist[3][startLine:]
DEClist = TSVlist[4][startLine:]
OFFSETlist = TSVlist[5][startLine:]
BROADCOUNTlist = TSVlist[6][startLine:]
SOFTCOUNTlist = TSVlist[7][startLine:]
MEDCOUNTlist = TSVlist[8][startLine:]
HARDCOUNTlist = TSVlist[9][startLine:]

#produces error radii list from empirical formula found in Wong et al paper
#the offset and counts are both returned as strings with extra whitespace at the start
#so they are clipped and turned into floats for the computation
errRADIIlist = []
for i in range(len(COUNTlist)):
	radii = 0 
	radii = (0.25 + 
			(0.1 / math.log(float(BROADCOUNTlist[i][2:])+1, 10)) *
			(1 + (1 / math.log(float(BROADCOUNTlist[i][2:])+1, 10))) +
			(0.03 * (float(OFFSETlist[i][2:]) / math.log(float(BROADCOUNTlist[i][2:]) + 2, 10)) ** 2) +
			(0.0006 * (float(OFFSETlist[i][2:]) / math.log(float(BROADCOUNTlist[i][2:]) + 3, 10)) ** 4)
			)
	errRADIIlist.append(radii)


# print(NAMElist)
# print(RAlist)
# print(DEClist)
# print(COUNTlist)
# print(OFFSETlist)
# print(errRADIIlist)


#starts the list of lines that go into the region file
regionFileList=[]
regionFileList.append("""# Region file format: DS9 version 4.1
global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1
fk5""")

#adds circles for each source
#each region is given it's name from the source list
#the radius of each region circle is given from the source list in arcsecs (NOT WORKING RIGHT YET)
for i in range(len(NAMElist)):
	line = ("circle(" +
			RAlist[i][1:3] + ":" + RAlist[i][4:6] + ":" + RAlist[i][7:] + "," +
			DEClist[i][:3] + ":" + DEClist[i][4:6] + ":" + DEClist[i][7:] + "," +
			str(errRADIIlist[i]) + "\"" +
#			str(4) + "\"" +
			")" + " # text={" + NAMElist[i] + "}"
		   )
	regionFileList.append(line)


#saves the region file list of lines to region file
with open(inputTSV[:-3] + "reg",'w') as file:
    for item in regionFileList:
        print>>file, item
print("Done! Region file saved in same directory as TSV.")