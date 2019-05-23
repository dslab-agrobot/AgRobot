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
from tools.imgSplice import splice_h,splice_v

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
x = 0

step_y = 3
print(np.array(files))
try:
    for t in range(int(files.__len__() / step_y)):
        t1 = files[step_y * t].split('_')[2]

        # same method with picAll
        if x % 2 == 0:
            p_l = cv2.imread(basedir + files[step_y * t + step_y - 1])[:, 0:1280]
            for i in range(step_y - 1 ):
                p_r = cv2.imread(basedir + files[-i + step_y * t + step_y - 2])[:, 0:1280]
                p_l = splice_h(p_l, p_r)
        else:
            p_l = cv2.imread(basedir + files[step_y * t])[:, 0:1280]
            for i in range(step_y - 1):
                p_r = cv2.imread(basedir + files[i + step_y * t + 1])[:, 0:1280]
                p_l = splice_h(p_l, p_r)
            # p_l = cv2.imread(basedir + files[3 * t])[:, 0:1280]
            # p_m = cv2.imread(basedir + files[3 * t + 1])[:, 0:1280]
            # p_r = cv2.imread(basedir + files[3 * t + 2])[:, 0:1280]
        x += 1
        cv2.imwrite(basedir + 'temp/' + t1 + '.jpg', p_l)
except Exception:
    print('pictures are crappy')
#
#
# for _, _, files in os.walk(pj(basedir, 'temp/')):
#     break
# files = sorted(files)
# try:
#     for t in range(int(files.__len__() - 1)):
#         t1 = files[t+1]
#         # same method with picAll
#         p_l = cv2.imread(pj(basedir, 'temp/')+ files[t])
#         p_r = cv2.imread(pj(basedir, 'temp/') + files[t+1])
#         p1 = splice_v(p_l, p_r)
#         if t == int(files.__len__() - 2):
#             cv2.imwrite(basedir + 'temp/finally.jpg', p1)
#         else:
#             cv2.imwrite(basedir + 'temp/' + t1 + '.jpg', p1)
# except Exception:
#     print('pictures are crappy')


