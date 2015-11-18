from subprocess import call
from optparse import OptionParser as opt
import os

prsr = opt()
prsr.add_option("-m", "--meta", dest="meta", metavar="FILE", help="Meta data in EXCEL format. Should be structured as used in scan-o-matic with 4 tabs")
prsr.add_option("-i", "--input", dest="curves", metavar="FILE", help="Input file with curve data. Select either curves_raw.npy for raw curves, or curves_smooth.npy for smoothened curves.")
prsr.add_option("-p", "--plate", dest="no", metavar="INT", help="Plate (0-3) to process")
prsr.add_option("-o", "--output", dest="path", metavar="PATH", default=os.getcwd(), help="Output path Default:%default")
(options, args) = prsr.parse_args()

DEVNULL = open(os.devnull, 'wb')

extracter = os.path.join(os.path.dirname(os.path.abspath(__file__)),extract.curves.py)
plotter = os.path.join(os.path.dirname(os.path.abspath(__file__)),plot_curves.r) 


call(["python", extracter], stdout=DEVNULL, stderr=DEVNULL)
call(["Rscript", plotter], stdout=DEVNULL, stderr=DEVNULL)
