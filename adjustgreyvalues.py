###############################################################################
# Name        : greycorrect.py                                                #
# Author      : Yasin Gamieldien                                              # 
# Description : Correction of grey values above or below certain threshold as #
# Notes       : Written with Python 3.4 on Ubuntu 15.10 but should be         #
#               compatible with Python 2.7, minor adjustments for filesytem   #
#               possibly required for other platforms                         #
# Required    : numpy                                                         #
# Date        : 3 November 2015                                               #
###############################################################################

from PIL import Image
import numpy as np
import os
PATH = "~/pics/" #Specify path

files = os.listdir(PATH) #Reads files in as stack
files.sort()

NEWPATH =  "~/pics/edit/" #Change as required

if not os.path.exists(NEWPATH):
    os.mkdir(NEWPATH)

#An error is produced if PATH contains non-image files - no corrections made as
#images are meant to be handled in one single batch from a dedicated directory
#This includes directories - can be corrected by selecting appropriate extension

for x in files:
    im = Image.open(PATH+x)
    im = im.convert("L")
    imarray = np.array(im)
    imarray[imarray>128] = 255 #Corrects grey values above specified range
    outFile = Image.fromarray(imarray)
    outFile.save(NEWPATH+x) #Writes to new files
