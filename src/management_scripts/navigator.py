"""
Navigator to control robot to move and act


__copyright__="Jiangxt"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


Simple Use this script by :
```
python navigator.py X 100 # direction and length
```


Use ths script by:
```
nav = Navigator()
nav.move_x(DISTANCE)
nav.move_y(DISTANCE)
```


"""

import tools.connector
import argparse


#
def move_x(dis):

    cmd = "X"
    if dis >= 0 :
        if dis < 10 :
            cmd += '+00'
        elif dis <100 :
            cmd += '+0'
        else:
            cmd += '+'
    else:
        if dis > -10 :
            cmd += '-00'
        elif dis > -100:
            cmd += '-0'
        else :
            cmd += '-'
    cmd += str(abs(dis))
    print(cmd)
    # return s.send_cmd(cmd.encode("ascii"))



def move_y(dis):
    cmd = "Y"
    if dis >= 0:
        if dis < 10:
            cmd += '+00'
        elif dis < 100:
            cmd += '+0'
        else:
            cmd += '+'
    else:
        if dis > -10:
            cmd += '-00'
        elif dis > -100:
            cmd += '-0'
        else:
            cmd += '-'
    cmd += str(abs(dis))
    print(cmd)
    # return s.send_cmd(cmd.encode("ascii"))

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print (args.square**2)

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()

