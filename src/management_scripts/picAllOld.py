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

import sys,time

# without package management in version-0.1 , we need to
# append system path for our scripts
sys.path.append("/home/magic-board/Desktop/AgRobot-master/src/management_scripts/")
sys.path.append("/home/magic-board/Desktop/AgRobot-master/src/tools/")

from management_scripts import navigator
# import python script by absolute path due to using crontab

from tools import imgRec

STEP_X = -500  # each step for 12m side in mm
STEP_Y = -70  # each step for 1m side in mm


WALK_X = 2  # max walks for 12m side
WALK_Y = 2  # max walks for 1m side

# init a recoder to take and join photos
Recoder = imgRec.ImgRec()

# init a navigator to control robot
nav = navigator.Navigator()

# aimed at saving energy , we decided to move robot's y-aix
# more often , and move like by S route.
# S route for (x,y) like :
# (0,0) (0.5,0.25) (0.5,0.5) (0.5,0.75)
# (1,0.75) (1.0,0.5) .....  (11.5,0.75)

w_x = 0  # current walk in x
w_y = 0  # current walk in y
dir_y = 1  # direction for y

# when finished walking in y , change dir NEXT TIME
_preChange_y = True

"""
↑   ┏━━━━┓   ┏━━━━┓
Y   ┃    ┃   ┃    ┃ 
X→       ┗━━━┛    ┗━━━┛
move like curve up there 
what a beautiful art , (ฅ•-•ฅ) , isn't it?
"""

# use a boolean to control robot not to turn back
# immediately when finished y
for w_x in range(WALK_X):
    for w_y in range(WALK_Y):
        # new dir has been set but not move when it start
        if _preChange_y:
            _preChange_y = False
        else:
            nav.move_y(dir_y * STEP_Y)
        Recoder.capture_frame()
    _preChange_y = True
    # set the contrary of original direction
    dir_y *= -1
    nav.move_x(STEP_X)


# it will close and release cameras' resources by itself
del Recoder







