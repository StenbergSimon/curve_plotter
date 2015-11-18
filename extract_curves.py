# Importing some required libraries 
import pandas as pd
import numpy as np
from optparse import OptionParser as opt
import os

# This part handles the flags for input and such
prsr = opt()
prsr.add_option("-m", "--meta", dest="meta", metavar="FILE", help="Meta data in EXCEL format. Should be structured as used in scan-o-matic with 4 tabs")
prsr.add_option("-i", "--input", dest="curves", metavar="FILE", help="Input file with curve data. Select either curves_raw.npy for raw curves, or curves_smooth.npy for smoothened curves.")
prsr.add_option("-p", "--plate", dest="no", metavar="INT", help="Plate (0-3) to process")
prsr.add_option("-o", "--output", dest="path", metavar="PATH", default=os.getcwd(), help="Output path Default:%default")
(options, args) = prsr.parse_args()

# Here some functions are defined

#This function assigns row and column numbers to each row in the meta data
def annotate_pos(table, plate_no):
	plate = table[list(table.viewkeys())[int(plate_no)]]
	plate['Column'] = range(0,48)*32
	rows = []
	for i in range(0,32):
        	for n in range(0,48):
                	rows.append(i)
	plate['Row'] = rows
	return plate

# This fuction extracts the curves
def extract_curves(curves, meta_data, plate_no, outpath):
        for ORF in meta_data[0].unique():
		temp_table = meta_data.loc[meta_data[0] == ORF]
		df = pd.DataFrame()
		i = 1
		for row,col in zip(temp_table['Row'], temp_table['Column']):
			entry = str(ORF) + str(i)
			df[entry] = curves[plate_no][row][col]
			i = i + 1
		df.to_csv(os.path.join(os.path.abspath(outpath),str(ORF)))
		


# Here the script reads the files and store them in memory
meta_data = pd.read_excel(options.meta, sheetname=None, header=None)
curves = np.load(options.curves)

# Here the program actually runs
plate = annotate_pos(meta_data, options.no)
extract_curves(curves, plate, options.no, options.path)

