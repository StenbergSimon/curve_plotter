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
def extract_curves(curves, meta_data, plate_no, outpath, norm, over):
        for ORF in meta_data[0].unique():
		files.append(ORF)
		temp_table = meta_data.loc[meta_data[0] == ORF]
		df = pd.DataFrame()
		i = 1
		for row,col in zip(temp_table['Row'], temp_table['Column']):
			entry = str(ORF) + str(i)
			df[entry] = curves[plate_no][row][col]
			i = i + 1
		if bool(norm) and bool(over):
			df=norm_global(df,plate_no,curves)
		elif bool(norm):
			df = norm_amp(df)
		df.to_csv(os.path.join(os.path.abspath(outpath),str(ORF)))

def norm_amp(df):
	z = max(df.loc[0,]) - df.loc[0,]
	df = z + df
	return df

def norm_global(df,plate_no, curves):
	zeroes = []
	for i in range(0,48):
    		for n in range(0,32):
        		zeroes.append(curves[0][n][i][0])
	m = max(zeroes)
	z = m - df.loc[0,]
	df = z + df
	return df
