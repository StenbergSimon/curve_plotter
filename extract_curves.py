# Importing some required libraries 
import os
import pandas as pd

# List each ORF
files = []

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
		files.append(ORF)
		temp_table = meta_data.loc[meta_data[0] == ORF]
		df = pd.DataFrame()
		i = 1
		for row,col in zip(temp_table['Row'], temp_table['Column']):
			entry = str(ORF) + str(i)
			df[entry] = curves[plate_no][row][col]
			i = i + 1
		df.to_csv(os.path.join(os.path.abspath(outpath),str(ORF)))
		

