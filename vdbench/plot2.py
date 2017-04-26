import subprocess
import matplotlib
import csv
import pandas as pd
import sys
import yaml

matplotlib.use('Agg')

inputpath=sys.argv[1]

inputFile=open(inputpath,'r')
dataMap=yaml.load(inputFile)

outputCSV=dataMap['csvdestination']
outputDir=dataMap['outputDir']
outputPlots=dataMap['graphs']

from matplotlib import pyplot as plt
def parseflat():
	subprocess.call("./vdbench parse -i %s/flatfile.html -c run interval reqrate rate resp MB/sec Read_rate Read_resp Write_rate Write_resp MB_read MB_write Xfersize Mkdir_rate Mkdir_resp Rmdir_rate Rmdir_resp Create_rate Create_resp Open_rate Open_resp Close_rate Close_resp Delete_rate Delete_resp Getattr_rate Getattr_resp Setattr_rate Setattr_resp  Copy_rate  Copy_resp  Move_rate  Move_resp  compratio dedupratio   cpu_used   cpu_user cpu_kernel   cpu_wait   cpu_idle -f -o %s" %(outputDir,outputCSV) ,shell=True)
	return




data = pd.read_csv('out2.csv')

def plot():
	
	plt.plot(data['rate'])
	plt.title('Rate')
	plt.ylabel('Rate')
	plt.xlabel('Time')
        rate=outputPlots+"/Rate.png"
	#plt.show()
        plt.savefig(rate)
	
	plt.plot(data['MB_read'])
        plt.title('MB_Read')
        plt.ylabel('MB_Read')
        plt.xlabel('Time')
	MB_read=outputPlots+"/MB_read.png"
        plt.savefig(MB_read)
	

	plt.plot(data['Read_resp'],label="Read_Response_Time")
	plt.plot(data['Read_rate'],label="Reads_Per_Second")
	plt.plot(data['rate'])
	plt.plot(data['MB_read'])
	
	plt.title('Reads')
        plt.xlabel('Time')
	plt.ylabel('Quantity')
	plt.legend()
	Reads=outputPlots+"/Reads.png"
        plt.savefig(Reads)
	return


def main():
	parseflat()
	plot()
	return


main()

