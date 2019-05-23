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
<<<<<<< HEAD:src/management_scripts/navigator.py
import sys,time
sys.path.append('/home/pi/Desktop/AgRobot/src')
from tools.connector import RpiArdConnector
=======

from tools.connector import send_msg
>>>>>>> jiangxt:src/tools/navigator.py
import argparse
import pandas as pd

class Navigator(object):
    """Navigator to control the robot

    1). control robot to MOVE forward,backward,rightward,leftward
    2). control robot to ROTATE the camera
    3). control robot to LIGHT led light

    Attributes:
        ser_timeout: time out of response to serial

    """

    def __init__(self):
<<<<<<< HEAD:src/management_scripts/navigator.py
        self.conn = RpiArdConnector()
=======

        # we need to load position from a log last time

        self._x = 0
        self._y = 0
        try:
            df = pd.read_csv('nav.log', index_col=0, header=None,
                         parse_dates=True, squeeze=True).to_dict()
            self._x = df['X']
            self._y = df['Y']
        finally:
            pass

>>>>>>> jiangxt:src/tools/navigator.py

    def __del__(self):

        self.write_log()

    def move_x(self, dis):

        cmd = "X"
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
<<<<<<< HEAD:src/management_scripts/navigator.py
        conn = RpiArdConnector()
        time.sleep(2)
        msg= conn.send_msg(cmd.encode("ascii"))
        del conn
        return msg
=======
        return send_msg(cmd.encode("ascii"))

>>>>>>> jiangxt:src/tools/navigator.py
    def move_y(self, dis):
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
<<<<<<< HEAD:src/management_scripts/navigator.py
        print (cmd)
        conn = RpiArdConnector()
        time.sleep(2)
        msg= conn.send_msg(cmd.encode("ascii"))
        del conn
        return msg
=======
        return send_msg(cmd.encode("ascii"))

    def write_log(self):
        log ={'X': self.pos_x, 'Y': self.pos_y}
        pd.Series(log).to_csv('nav.log', header=False)

>>>>>>> jiangxt:src/tools/navigator.py

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("dir", help="direction of it's movement", type=str, choices=['x', 'X', 'y', 'Y'])
    # parser.add_argument("len", help="length of it's movement ", type=int)
    # args = parser.parse_args()
    nav = Navigator()
<<<<<<< HEAD:src/management_scripts/navigator.py
    if args.dir == 'x' or args.dir == 'X':
        nav.move_x(args.len)
    else:
        nav.move_y(args.len)
=======
    del nav
    # if args.dir == 'x' or args.dir == 'X':
    #     print(nav.move_x(args.len))
    # else:
    #     print(nav.move_y(args.len))

>>>>>>> jiangxt:src/tools/navigator.py

