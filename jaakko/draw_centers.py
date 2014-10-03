from ij import IJ
from ij.gui import PointRoi

from java.awt import Color

import csv
import math
import os
import sys

LINE_DX = 400

def draw_centers(data):
    pathname = data[1]
    filename = data[2]
    platename = data[3]

    nx = int(data[4])
    ny = int(data[5])
    ax = int(data[6])
    ay = int(data[7])
    
    orientation = 2*math.pi * float(data[8]) / 360.0
    line_dy = int(round(math.atan(orientation) * LINE_DX))
    ax2 = ax - LINE_DX
    ay2 = ay - line_dy

    orientation_avg = 2*math.pi * float(data[9]) / 360.0
    line_dy = int(round(math.atan(orientation_avg) * LINE_DX))
    ax3 = ax - LINE_DX
    ay3 = ay - line_dy

    imp = IJ.openImage(os.path.join(pathname,filename))

    roi_nucleus = PointRoi(nx,ny)
    roi_nucleus.setDefaultMarkerSize("Large")
    roi_nucleus.setStrokeColor(Color.CYAN)
    roi_anchor = PointRoi(ax,ay)
    roi_anchor.setDefaultMarkerSize("Large")
 
    imp.getProcessor().drawRoi(roi_nucleus)
    imp.getProcessor().drawRoi(roi_anchor)

    imp.setColor(Color.RED)
    imp.getProcessor().drawLine(ax,ay,ax2,ay2)
    imp.setColor(Color.WHITE)
    imp.getProcessor().drawLine(ax,ay,ax3,ay3)


    IJ.saveAsTiff(imp,os.path.join(pathname,filename))

f = open(sys.argv[1], 'rb') 
try:
    reader = csv.reader(f,quotechar="'")
    for row in reader:
        draw_centers(row)
        #sys.exit()
finally:
    f.close()
