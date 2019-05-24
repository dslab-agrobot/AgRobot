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
import sys
# without package management in version-0.1 , we need to
# append system path for our scripts
sys.path.append("/home/magic-board/Desktop/AgRobot-master/src")
from tools.connector import RpiArdConnector
import argparse


# MAX Length for 12m side with mm
MAX_X = 1200
# MAX Length for 1m side with mm
MAX_Y = 100


class Navigator(object):
    """Navigator to control the robot

    1). control robot to MOVE forward,backward,rightward,leftward
    2). control robot to ROTATE the camera
    3). control robot to LIGHT led light

    Attributes:
        ser_timeout: time out of response to serial

    """

    def __init__(self):
        self.conn = RpiArdConnector()
        # we need to load position from a log last time
        self._x = 0
        self._y = 0

    def __del__(self):
        del self.conn

    @property
    def pos_x(self):
        """RO position for X

        :return: current pos for x
        """
        return self._x

    # hide this x set function for only check by this script
    def __delta_x(self,v):
        new_v = self._x + v
        if new_v > MAX_X or new_v <= 0:
            print('X !!! %d',new_v)
        else:
            self._x = new_v


    @property
    def pos_y(self):
        """RO position for Y

        :return: current pos for y
        """
        return self._y

    # same with y
    def __delta_y(self, v):
        new_v = self._y + v
        if new_v > MAX_Y or new_v <= 0:
            print('Y !!! %d', new_v)
        else:
            self._y = new_v

    def move_x(self, dis):
        self.__delta_x(dis)
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
        return self.conn.send_msg(cmd.encode("ascii"))

    def move_y(self, dis):
        self.__delta_y(dis)
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
        return self.conn.send_msg(cmd.encode("ascii"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="direction of it's movement", type=str, choices=['x', 'X', 'y', 'Y'])
    parser.add_argument("len", help="length of it's movement ", type=int)
    args = parser.parse_args()
    nav = Navigator()
    if args.dir == 'x' or args.dir == 'X':
        print(nav.move_x(args.len))
    else:
        print(nav.move_y(args.len))


