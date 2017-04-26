######################################################################################## 
#Script to parse the YAML file and to set the
# paramters in the paramFile for the vdbench test suite
# The destination directories like output for vdbench, graphs, csv, param are 
# taken from the YAML file itself to make it more generic

########################################################################################

import yaml
import subprocess
import sys

# Scan the command line input

inputpath=sys.argv[1]

inputFile=open(inputpath,'r')
dataMap=yaml.load(inputFile)

# Set the output directories for param and vdbench output files

paramFile=dataMap['paramFile']
outputDir=dataMap['outputDir']

def createParam():
	
	outputFile=open(paramFile,'w+')

# Parse the storage, workload and run definitions

	storageDefinition= "fsd="+dataMap['SDName']+","+"anchor="+dataMap['Anchor']+","+"depth="+dataMap['Depth']+","+"files="+dataMap['Files']+","+"size="+dataMap['Size']+","+"width="+dataMap['Width']+"\n"

	workDefinition= "fwd="+dataMap['WDName']+","+"fsd="+dataMap['SDForWD']+","+"rdpct="+dataMap['ReadPercentage']+","+"xfersize="+dataMap['TransferSize']+","+"fileio="+dataMap['FileIO']+","+"threads="+dataMap['Threads']+","+"fileselect="+dataMap['FileSelect']+"\n"


	runDefinition= "rd="+dataMap['RDName']+","+"fwd="+dataMap['WDForRD']+","+"elapsed="+dataMap['Duration']+","+"interval="+dataMap['Interval']+","+"fwdrate="+dataMap['Fwdrate']+","+"format="+dataMap['Format']+"\n"

# write into the paramFile

	outputFile.write(storageDefinition)	
	outputFile.write(workDefinition)
	outputFile.write(runDefinition)

	outputFile.close()
	inputFile.close()
	return

# Run the vdbench test suite

def runtest():
	
	subprocess.call("./vdbench -f %s -o %s" %(paramFile,outputDir),shell=True)
	return

# Run the plotting script

def callPlot():
	subprocess.call("python plot2.py %s" %(paramFile),shell=True)
	return

def main():
	createParam()
	runtest()
	#callPlot()
	return 
	

main()

