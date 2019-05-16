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
import serial
# import python script by absolute path due to using crontab
sys.path.append("/home/magic-board/src/tools/ai/")

STEP_X = 400  # each step for 12m side in mm
STEP_Y = 300  # each step for 1m side in mm


WALK_X = 2  # max walks for 12m side
WALK_Y = 0  # max walks for 1m side


w_x = 0  # current walk in x
w_y = 0  # current walk in y


class Ser(object):

    def __init__(self):
        self.port = serial.Serial(port='/dev/ttyACM0', baudrate=115200,
                                  timeout=2)
        time.sleep(2)

    def send_cmd(self, cmd):
        self.port.write(cmd)

        response = self.port.readall()
        #response = self.convert_hex(response)
        return response

    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))

        return result

s = Ser()




# init a recoder to take and join photos
#Recoder = imgRec.ImgRec()
#
#for w_y in range(WALK_Y):
#
#    # move half step if neighbor to the border
#    if w_y == 0 or w_y == WALK_Y-1:
#        move_y(STEP_Y/2)
#        pass
#    else:
#        move_y(STEP_Y)
#        pass
#
#    for w_x in range(WALK_X):
#
#        # move half step if neighbor to the border
#        if w_x == 0 or w_x == WALK_X - 1:
#            move_x(STEP_X/2)
#            pass
#        else:
#            move_x(STEP_X)
#            pass
#
#        # take photos in longer side makes it ..... energy-saving
#        Recoder.capture_frame()
#
## it will close and release cameras' resources by itself
#del Recoder








