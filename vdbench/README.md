# Storage Testing using vdbench

The module aims at automating storage tests using the vdbench tool. It is built with the intent of 
making the process easier and generic. 

## About vdbench

**Vdbench** is a disk I/O workload generator to be used for testing and benchmarking of existing
and future storage products. The objective of Vdbench is to generate a wide variety of controlled storage I/O workloads,
allowing control over workload parameters such as I/O rate, LUN or file sizes, transfer sizes,
thread count, volume count, volume skew, read/write ratios, read and write cache hit
percentages, and random or sequential workloads.

To learn more about vdbench : click [here](https://github.com/openebs/test-storage/blob/master/vdbench/vdbench.pdf)

## Editing the YAML file

* Set the destination of output directories : {outputDir, paramFile, csvdestination, graphs}
* Set the input paramters for the vdbench test suite : SD, WD, RD

## How to use the module

* Edit the YAML file to set the paramters to *vdbench* suite
* Run the python script using this
```
python parseYAML.py <path-to-YAML-file>
```

* The output of vdbench will be in the folder specified in *outputDir* 
* The parameter file for the vdbench will be in the path specified in *paramFile*

* To get a sample plot of basic paramters, execute
```
python plot.py <path-to-YAML-file>
```

* The plots will be in the directory specified in *graphs* 
* The parsed CSV of the flatfile.html will be stored in the place specified in *csvdestination*
* The CSV files can be used later for analysis of *storage performance*

## About the Code

Libraries used:

* yaml: For read/write of YAML files
* pandas: For accessing,reading, parsing CSV files and creating data frames
* matplotlib: Plotting graphs and data visualization

If these have not been installed, install them using the commands:

```
sudo apt-get install python-pip
sudo pip install yaml
sudo pip install numpy
sudo pip install pandas
sudo pip install matplotlib
```
