# coding: utf-8
"""
Splice two images by open-cv
__copyright__="Jiangxt"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


```
Use this script by :
```
# Splice two images in horizon
imgSplice.splice_h(IMAGE_LEFT,IMAGE_RIGHT)

# Splice two images in vertical
imgSplice.splice_w(IMAGE_UP,IMG_DOWN)
```

"""
import sys, os, shutil
import numpy as np
import cv2
from os.path import join as pj
import imgSplice

# without package management in version-0.1 , we need to
# append system path for our scripts
sys.path.append("/home/pi/Desktop/AgRobot/src/tools")
basedir = '/home/jc/Pictures/h/'

# check for temp folder exist for temp works
if os.path.exists(pj(basedir, 'temp')):
    shutil.rmtree(pj(basedir, 'temp'))
os.mkdir(pj(basedir, 'temp'))

files = []
for _, _, files in os.walk(basedir):
    break

files = sorted(files)

file_head = '_'.join(files[0].split('_')[0:2])

for t in range(int(files.__len__()/2)):
    t1 = files[2*t].split('_')[2]
    print(files[2*t],files[2*t+1])
    p_r = cv2.imread(basedir + files[2*t])[:, 0:1280]
    p_l = cv2.imread(basedir + files[2 * t+1])[:, 0:1280]
    p = imgSplice.splice_h(p_l, p_r)
    cv2.imwrite(basedir + 'temp/' + t1 + '.jpg', p)
    # break

print(file_head)
