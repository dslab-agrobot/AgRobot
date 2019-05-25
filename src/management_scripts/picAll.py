"""
Take photos for the whole field


__copyright__="Jiangxt""weiyq"
__email__ = "<jiangxt404@qq.com>""<wyq_l@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```
$ chmod +x absPath/picAll.py    # make this script run-able
$ crontab -e                    # write these cmd in

30 8 * * * python absPath/picAll.py     # run 8:30  am per day
# add some more daily running
```


------------------------------------------------------------
ATTENTION PLEASE

-----------------------------------------|
left side                                |
|----------|                             |
|          |          soil               |
|      car |                             |
|----------|    KG                       |
right side                               |               huyang DOOR 
------------------------------------------

You need set up the cameras as wrote in src/tools/ai/imgRec.py
Edit crontab with 'crontab -e' as below, then it can be executed automatic
before run this python file ,make sure the Y positon is on 250 at the left side 
------------------------------------------------------------

"""

import sys,time,os,argparse
# without package management in version-0.1 , we need to
# append system path for our scripts
sys.path.append("/home/pi/AgRobot/src/management_scripts/")
sys.path.append("/home/pi/AgRobot/src/")
sys.path.append("/home/pi/AgRobot/src/tools")
from tools import dir
from tools import navigator
# import python script by absolute path due to using crontab

from imgRec import capture_frame,capture_video
STEP_X = 150  # each step for 12m side in mm
STEP_Y = 250  # each step for 1m side in mm

# current file path
base_path = os.path.split(os.path.realpath(__file__))[0]
WALK_X = 30  # max walks for 12m side


def execute():
    # init a navigator to control robot
    nav = navigator.Navigator()
    # pics saved path
    path = base_path+'/' + dir.cur_time()
    # mkdir new path for saving pics
    dir.mkdir(path)

    folders = []
    for _, folders, _ in os.walk(path):
        break
    path += '/' + str(folders.__len__())
    dir.mkdir(path)
    
    # aimed at saving energy , we decided to move robot's y-aix
    # more often , and move like by S route.
    # S route for (x,y) like :
    # (0,0) (0.5,0.25) (0.5,0.5) (0.5,0.75)
    # (1,0.75) (1.0,0.5) .....  (11.5,0.75)

    w_x = 0  # current walk in x
    w_y = 250  # current walk in y
    dir_y = -1  # direction for y

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
        # need shot 3 times on Y direction
        if (w_x % 2 == 0):
            capture_frame(None, w_x, 0, path)
            # time.sleep(3)
            nav.move_y(dir_y * STEP_Y)
            time.sleep(4)
            capture_frame(None, w_x, 1, path)
            # time.sleep(3)
            nav.move_y(dir_y * STEP_Y)
            time.sleep(4)
            capture_frame(None, w_x, 2, path)
        else:
            capture_frame(None, w_x, 2, path)
            # time.sleep(3)
            nav.move_y(dir_y * STEP_Y)
            time.sleep(4)
            capture_frame(None, w_x, 1, path)
            # time.sleep(3)
            nav.move_y(dir_y * STEP_Y)
            time.sleep(4)
            capture_frame(None, w_x, 0, path)
        dir_y = dir_y * -1
        # time.sleep(3)
        nav.move_x(STEP_X)
        time.sleep(4)
        # log('20190521_14/20/43  move_Y_from_?_to_?  success/failed ')

    del nav


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="direction of it's movement", type=str, choices=['+', '-'],default='+')
    args = parser.parse_args()
    if args.dir == '-':
        STEP_X = -STEP_X
    execute()
