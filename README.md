# curve_plotter

Plot scan-o-matic curves of a specific plate, grouped by meta data

By: Simon Stenberg, 2015

# Dependencies:

_python:_
pandas
numpy

_R:_
Rmisc
ggplot2

# Install:

In the terminal. Write:

	git clone [URL found on the right panel]


# Instructions:

You need to have the numpy curves file from scan-o-matic. Either curves_raw.npy or curves_smooth.npy should work.

Secondly, you need the meta data as to be used in scan-o-matic in excel format (.xlsx) with 1 tab for each plate.

Use the plotter_wrapper.py to plot either all curves separatly, or together.

To get the help message, type:
	
	python plotter_wrapper.py -h

output:

	Usage: plotter_wrapper.py [options]
	
	Options:
	  -h, --help            show this help message and exit
	  -m FILE, --meta=FILE  Meta data in EXCEL format. Should be structured as
	                        used in scan-o-matic with 4 tabs
	  -i FILE, --input=FILE
	                        Input file with curve data. Select either
	                        curves_raw.npy for raw curves, or curves_smooth.npy
	                        for smoothened curves.
	  -p INT, --plate=INT   Plate (0-3) to process
	  -o PATH, --output=PATH
	                        Output path Default:/Users/Simon/git/curve_plotter
	  -n                    Set True to push amplitude of all curves to the
	                        highest one.
	  -z                    Plot overlay?
	  -r                    Remove data files?
	

* -m is where you input the meta data
* -i is where you input the curve data
* -p is the plate that should be analyzed, all other plates are completly disregarded.
* -o is where to output all the plot and intermediate data files. Defaults to where the script is run.
* use the flag -n to normalize amplitude of curves. This will add the difference between the highest initial cell value in the series and each initial cell value to all values in the series. That wil push all curves to the same starting cell count.
* use -z to plot all curves in one plot, color coded for each strain/meta-data
* use -r to keep all data files. The data files are simple text files with a column for each curve for each replicate, theese will be saved in ouput path.

# Examples

	python plotter_wrapper.py -m meta_data.xlsx -i curves_smooth.npy -p 0 -n -r

The above command will extract all curves with the same meta data annotation in meta_data.xlsx for plate 1 (0). It will then normalize the curves in y-led and plot the average curve for each meta data annotation and the standard deviation as a shaded area around the line. It will only keep the pdfs with plots.

	python plotter_wrapper.py -m meta_data.xlsx -i curves_smooth.npy -p 0 -n -z

The above command will work as the previous command, but each average curve will be plotted in the same graph. Also, the data files with curves will be kept where the script is run.
