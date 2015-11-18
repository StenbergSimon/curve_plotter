from subprocess import call
from optparse import OptionParser as opt
import os
import extract_curves
import pandas as pd
import numpy as np

prsr = opt()
prsr.add_option("-m", "--meta", dest="meta", metavar="FILE", help="Meta data in EXCEL format. Should be structured as used in scan-o-matic with 4 tabs")
prsr.add_option("-i", "--input", dest="curves", metavar="FILE", help="Input file with curve data. Select either curves_raw.npy for raw curves, or curves_smooth.npy for smoothened curves.")
prsr.add_option("-p", "--plate", dest="no", metavar="INT", help="Plate (0-3) to process")
prsr.add_option("-o", "--output", dest="path", metavar="PATH", default=os.getcwd(), help="Output path Default:%default")
prsr.add_option("-n", "--norm_amp", dest="norm", metavar="BOOLEAN", default="False", help="Set True to push amplitude of all curves to the highest one. Default:%default")
(options, args) = prsr.parse_args()

if __name__ == "__main__":
	DEVNULL = open(os.devnull, 'wb')

	meta_data = pd.read_excel(os.path.abspath(options.meta), sheetname=None, header=None)
	curves = np.load(os.path.abspath(options.curves))
	plotter = os.path.join(os.path.dirname(os.path.abspath(__file__)),"plot_curves.r") 
	plate = extract_curves.annotate_pos(meta_data, options.no)
	extract_curves.extract_curves(curves, plate, options.no, options.path, options.norm)
	fh = open(os.path.join(options.path,"list"),w)
	for data in extract_curves.files:	
		fh.write("%s\n" % data)
		call(["Rscript", str(plotter), str(data)],stdout=DEVNULL, stderr=DEVNULL)
		call(["rm", str(data)])
