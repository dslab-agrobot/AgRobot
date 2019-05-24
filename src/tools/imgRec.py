"""
Capture img from two camera and join them for Agrobot
__copyright__="Jiangxt""weiyq"
__email__ = "<jiangxt404@qq.com>" "<wyq_l@qq.com>"
__license__ = "GPL V3"
__version__ = "0.2"
Simple test for this script :
```
python3 imgRec.py    # give a joined pic with date-time label
```
Use this script by :
```
recoder = recoder = ImgRec()
recoder.capture_frame()
```
------------------------------------------------------------
ATTENTION PLEASE
You need to plug the two camera with order in a raspberry-pi
due to open-cv made default index when it plugged.
Make Sure the FIRST one that be plugged should be the
HIGH RESOLUTION one .
------------------------------------------------------------
"""

import cv2
import datetime
import numpy as np
import os,re


def Zoom(frame, zoomSize):
    c_x = frame.shape[0] / 2
    c_y = frame.shape[1] / 2
    w_x = c_x / zoomSize
    w_y = c_y / zoomSize
    frame = frame[int(c_x - w_x):int(c_x + w_x), int(c_y - w_y):int(c_y + w_y)]
    frame = cv2.resize(frame, ((int(frame.shape[1] * zoomSize)),
                               (int(frame.shape[0] * zoomSize))))
    return frame


def __init__():
    """
    :return: cap_l , VideoCapture of lower one
             cap_h , VideoCapture of higher one
    """
    # default pos of camera position
    cap_l_pos = '/dev/video0'
    cap_h_pos = '/dev/video1'

    # The USB-identifier of two cameras
    # /dev/video0 - 046d_0825_418FC3B0
    # /dev/video1 - 046d_0825_F01A0590
    cap_l_name = '046d_0825_418FC3B0'
    cap_h_name = '046d_0825_F01A0590'

    # get current position of this script
    current = os.path.split(os.path.realpath(__file__))[0]
    dev_inf = os.popen(current + '/listall.sh')
    dev_inf = dev_inf.read().split('\n')[:]
    for st in dev_inf:
        if st.strip() == '':
            continue
        t_pos = st.split('-')[0].strip()
        t_name = st.split('-')[1].strip()
        if t_name == cap_l_name and re.match('/dev/video*', t_pos):
            cap_l_pos = st.split('-')[0]

        if t_name == cap_h_name and re.match('/dev/video*', t_pos):
            cap_h_pos = st.split('-')[0]
    dev.close()
    print(cap_l_pos, cap_h_pos)
    cap_l_pos = cap_l_pos.split('video')[1]
    cap_h_pos = cap_h_pos.split('video')[1]

    # open exist camera failed will raise an exception
    # but it will say nothing with zero camera
    cap_h = cv2.VideoCapture(cap_l_pos)
    cap_l = cv2.VideoCapture(cap_h_pos)

    # Try setting to higher resolution
    cap_h.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set the Horizontal resolution
    cap_h.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set the Vertical resolution
    cap_l.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # set the Horizontal resolution
    cap_l.set(cv2.CAP_PROP_FRAME_HEIGHT, 580)  # Set the Vertical resolution
    # cap_h.set(cv2.CAP_PROP_BUFFERSIZE,5)

    # Try setting to better effect of camera with high resolution
    cap_h.set(cv2.CAP_PROP_BRIGHTNESS, 0.4)
    cap_h.set(cv2.CAP_PROP_SATURATION, 0.3)
    cap_h.set(cv2.CAP_PROP_CONTRAST, 0.1)

    # Try setting to better effect of camera with low resolution
    cap_l.set(cv2.CAP_PROP_BRIGHTNESS, 0.2)
    cap_l.set(cv2.CAP_PROP_SATURATION, 0.1)
    cap_l.set(cv2.CAP_PROP_CONTRAST, 0.1)

    return cap_l, cap_h


def __del__(cap_l,cap_h):
    cap_h.release()
    cap_l.release()
    pass


def capture_frame(self, name, X, Y, path):
    """Capture and join pictures
    Get a picture of field by high-resolution camera , a picture of tape
    by low-resolution one , then crop the lower one into 80x80 pixes and
    put this into left-up corner of the higher one
    :param name:name of this picture ,default is YMD-H:M:S
    :param X:X position of this picture ,value will be a int ,in 0 - 31
    :param Y:Y position of this picture,value will be a int ,0 or 1
    :return: none
    :raise Exception:occur when at least one of camera can not be opened
    """

    cap_l, cap_h = __init__()
    # if camera does not open for some reason ,try 100 times,then raise an error
    for i in range(0, 100):
        if not (cap_l.isOpened() and cap_h.isOpened()):
            continue
        else:
            print("Cameras can  be  opened")
            break
    if i == 99:
        # todo,send mail to maillist
        raise Exception('Cameras can not be opened')
    # grab the frame with grab/retrieve so we can connect multiple
    # cameras and get roughly synchronized images

    # while (not(cap_h.grab() and cap_l.grab())) :
    ret_h = cap_h.grab()
    ret_h, frame_h = cap_h.retrieve()
    ret_l = cap_l.grab()
    ret_l, frame_l = cap_l.retrieve()

    # zoom this frame for remove
    frame_h = Zoom(frame_h, 1.05)

    # name the photo by date and time that we can make it easier for
    # recording and sorting

    if name is None:
        now_time = datetime.datetime.now()
        name = now_time.strftime("%Y%m%d_%H:%M:%S")
        name = name + '_X' + str(X) + '_Y' + str(Y)

    # show before joining
    # cv2.imshow('USB0-frame', frame_h)
    # cv2.imshow('USB1-frame', frame_l)

    # ROI range of the low resolution camera , the tape will be
    # capture at the corner of left-top roughly [0:80,0:80]
    # todo need to check
    roi = frame_l[230:320, :]

    # cv2.imwrite("low.jpg", frame_l)
    # cv2.imwrite("high.jpg", frame_h)
    # make a transpose
    roi = roi.transpose((1, 0, 2))

    # if we need flip in vertical
    # roi = roi[::-1]

    # if we need flip in horizon
    # roi = roi[::-1,::-1][::-1]
    print(roi.shape)
    # join the cropped frame and another one
    print(frame_h.shape)
    # frame_h[0:80, 0:479] = roi
    frame_n = np.zeros((720, 1370, 3))
    # frame_h[0:479,640:720] = roi
    frame_n[0:719, 0:1279] = frame_h
    frame_n[:640, 1280:] = roi
    # show after processing
    # cv2.imshow('JOIN-frame', frame_h)

    # write the joined picture with timed name

    cv2.imwrite(os.path.join(path, name + ".jpg"), frame_n)
    # log('20190521_14/20/43  shot_pic  success/failed ')
    # delete rets and frames
    # del ret_h,ret_l,frame_h,frame_l

    # do not forget to destroy windows after showing them
    # cv2.destroyWindow('USB0-frame')
    # cv2.destroyWindow('USB1-frame')
    # cv2.destroyWindow('ADD-frame')

def capture_video(self):
    # TBD
    pass
    
dev = os.popen("ls -l /dev/video* | awk '{print $10}'")
inf = dev.readline().strip()
dev.close()

# if __name__ == "__main__":
#
#     #for test
#     i = 0
#     X=0
#     Y=0
#     path='/home/pi/Desktop/AgRobot/src/tools/'
#     for i in range(1):
#         capture_frame(None,X,Y,path)
#



