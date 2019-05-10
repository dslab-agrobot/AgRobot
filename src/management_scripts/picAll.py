"""
Take photos for the whole field


__copyright__="Jiangxt"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```
$ chmod +x absPath/picAll.py    # make this script run-able
$ crontab -e                    # write these cmd in

30 8 * * * python absPath/picAll.py     # run 8:30 per day
# add some more daily running
```


------------------------------------------------------------
ATTENTION PLEASE

You need set up the cameras as wrote in src/tools/ai/imgRec.py
Edit crontab with 'crontab -e' as below, then it can be executed automatic
------------------------------------------------------------

"""

import sys

# import python script by absolute path due to using crontab
sys.path.append("/home/jc/Projects/AgRobot/src/tools/ai/")

import imgRec


def move_x(dis):
    pass


def move_y(dis):
    pass


STEP_X = 10  # each step for 12m side in mm
STEP_Y = 12  # each step for 1m side in mm


WALK_X = 40  # max walks for 12m side
WALK_Y = 10  # max walks for 1m side


# init a recoder to take and join photos
Recoder = imgRec.ImgRec()


w_x = 0  # current walk in x
w_y = 0  # current walk in y



for w_y in range(WALK_Y):

    # move half step if neighbor to the border
    if w_y == 0 or w_y == WALK_Y-1:
        move_y(STEP_Y/2)
        pass
    else:
        move_y(STEP_Y)
        pass

    for w_x in range(WALK_X):

        # move half step if neighbor to the border
        if w_x == 0 or w_x == WALK_X - 1:
            move_x(STEP_X/2)
            pass
        else:
            move_x(STEP_X)
            pass

        # take photos in longer side makes it ..... energy-saving
        Recoder.capture_frame()

# it will close and release cameras' resources by itself
del Recoder



