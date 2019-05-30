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

from connector import send_msg
import argparse
from imgRec import capture_frame,zone_check,RED_RANGES


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

        # we need to load position from a log last time

        self._x = 0
        self._y = 750
       # try:
       #     df = pd.read_csv('nav.log', index_col=0, header=None,
       #                  parse_dates=True, squeeze=True).to_dict()
       #     self._x = df['X']
       #     self._y = df['Y']
       # finally:
       #     pass


    def __del__(self):

        self.write_log()

    @property
    def pos_x(self):
        """RO position for X

        :return: current pos for x
        """
        return self._x

    # hide this x set function for only check by this script
    def __delta_x(self,v):
        new_v = self._x + v

        # [deprecated]
        # this can just avoid go to mush with little step-length
        # todo LASER FOR CHECK
        _, _, roi = capture_frame('', 0, 0, './')
        cnt, _, _ = zone_check(roi, RED_RANGES)

        if cnt > 300:
            print('Navigator: X detected red zone !')
            return 'forbidden'
        else:
            self._x = new_v
            return self._x


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
            print('Y seems wrong %d', new_v)
            return 'forbidden'
        else:
            self._y = new_v
            return self._y

    def move_x(self, dis):
        if self.__delta_x(dis) == 'forbidden':
            return 'forbidden'

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
        return send_msg(cmd.encode("ascii"))

    def move_y(self, dis):
        # if self.__delta_y(dis) == 'forbidden':
        #     return 'forbidden'

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
        return send_msg(cmd.encode("ascii"))

    def get_laser_pos(self):
        send_msg('71'.encode("ascii"), 'laser')
        return send_msg('01'.encode("ascii"), 'laser')

    def write_log(self):
        log ={'X': self.pos_x, 'Y': self.pos_y}
        #pd.Series(log).to_csv('nav.log', header=False)


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
    # print(nav.get_laser_pos())
    del nav

