import yaml
import subprocess
import sys


#paramFile="paramFile"
#outputDir="newdir"


inputpath=sys.argv[1]

inputFile=open(inputpath,'r')
dataMap=yaml.load(inputFile)

paramFile=dataMap['paramFile']
outputDir=dataMap['outputDir']

def createParam():
	
	outputFile=open(paramFile,'w+')

	storageDefinition= "fsd="+dataMap['SDName']+","+"anchor="+dataMap['Anchor']+","+"depth="+dataMap['Depth']+","+"files="+dataMap['Files']+","+"size="+dataMap['Size']+","+"width="+dataMap['Width']+"\n"

	workDefinition= "fwd="+dataMap['WDName']+","+"fsd="+dataMap['SDForWD']+","+"rdpct="+dataMap['ReadPercentage']+","+"xfersize="+dataMap['TransferSize']+","+"fileio="+dataMap['FileIO']+","+"threads="+dataMap['Threads']+","+"fileselect="+dataMap['FileSelect']+"\n"


	runDefinition= "rd="+dataMap['RDName']+","+"fwd="+dataMap['WDForRD']+","+"elapsed="+dataMap['Duration']+","+"interval="+dataMap['Interval']+","+"fwdrate="+dataMap['Fwdrate']+","+"format="+dataMap['Format']+"\n"

	outputFile.write(storageDefinition)	
	outputFile.write(workDefinition)
	outputFile.write(runDefinition)



	outputFile.close()
	inputFile.close()
	return

def runtest():
	#subprocess.call(["ls", "-l"])
	subprocess.call("./vdbench -f %s -o %s" %(paramFile,outputDir),shell=True)
	return

def callPlot():
	subprocess.call("python plot2.py %s" %(paramFile),shell=True)
	return

def main():
	createParam()
	runtest()
	#callPlot()
	return 
	

main()

