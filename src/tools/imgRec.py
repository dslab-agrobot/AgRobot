"""
Capture img from two camera and join them for Agrobot


__copyright__="Jiangxt; Zhip"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"

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


def Zoom(frame, zoomSize):
    c_x = frame.shape[0] / 2
    c_y = frame.shape[1] / 2
    w_x = c_x / zoomSize
    w_y = c_y / zoomSize
    frame = frame[int(c_x - w_x):int(c_x + w_x), int(c_y - w_y):int(c_y + w_y)]
    frame = cv2.resize(frame, ((int(frame.shape[1] * zoomSize)),
                               (int(frame.shape[0] * zoomSize))))
    return frame


class ImgRec(object):
    """ Image-Recoder for graping and joining images from two cameras


    """

    def __init__(self):
        # open exist camera failed will raise an exception
        # but it will say nothing with zero camera
        self.cap_h = cv2.VideoCapture(0)
        self.cap_l = cv2.VideoCapture(1)
        
        # Try setting to higher resolution
        self.cap_h.set(cv2.CAP_PROP_FRAME_WIDTH,1280) # set the Horizontal resolution
        self.cap_h.set(cv2.CAP_PROP_FRAME_HEIGHT,720) # Set the Vertical resolution
        self.cap_l.set(cv2.CAP_PROP_FRAME_WIDTH,640) # set the Horizontal resolution
        self.cap_l.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # Set the Vertical resolution
        
        # Try setting to better effect of camera with high resolution
        self.cap_h.set(cv2.CAP_PROP_BRIGHTNESS,10)
        self.cap_h.set(cv2.CAP_PROP_SATURATION,100)
        self.cap_h.set(cv2.CAP_PROP_CONTRAST,30)

        # Try setting to better effect of camera with low resolution
        self.cap_l.set(cv2.CAP_PROP_BRIGHTNESS,0)
        self.cap_l.set(cv2.CAP_PROP_SATURATION,50)
        self.cap_l.set(cv2.CAP_PROP_CONTRAST,35)

    def __del__(self):
        self.cap_h.release()
        self.cap_l.release()

    def capture_frame(self, name=None):
        """Capture and join pictures

        Get a picture of field by high-resolution camera , a picture of tape
        by low-resolution one , then crop the lower one into 80x80 pixes and
        put this into left-up corner of the higher one

        :param name:name of this picture ,default is YMD-H:M:S
        :return: none

        :raise Exception:occur when at least one of camera can not be opened
        """

        if not (self.cap_l.isOpened() and self.cap_h.isOpened()):
            raise Exception('Cameras can not be opened')
        
        # grab the frame with grab/retrieve so we can connect multiple
        # cameras and get roughly synchronized images
        ret_h = self.cap_h.grab()
        ret_h, frame_h = self.cap_h.retrieve()
        ret_l = self.cap_l.grab()
        ret_l, frame_l = self.cap_l.retrieve()

        # zoom this frame for remove
        frame_h =Zoom(frame_h, 1.05)

        # name the photo by date and time that we can make it easier for 
        # recording and sorting
        if name is None:
            now_time = datetime.datetime.now()
            name = now_time.strftime("%Y%m%d_%H:%M:%S")
        
        # show before joining
        # cv2.imshow('USB0-frame', frame_h)
        # cv2.imshow('USB1-frame', frame_l)
        
        # ROI range of the low resolution camera , the tape will be
        # capture at the corner of left-top roughly [0:80,0:80]
        roi = frame_l[0:80, 0:80]

        # join the cropped frame and another one
        frame_h[0:80, 0:80] = roi

        # show after processing
        # cv2.imshow('JOIN-frame', frame_h)
        
        # write the joined picture with timed name 
        cv2.imwrite(name + ".jpg", frame_h)
        
        # delete rets and frames
        del ret_h,ret_l,frame_h,frame_l
        
        # do not forget to destroy windows after showing them
        # cv2.destroyWindow('USB0-frame')
        # cv2.destroyWindow('USB1-frame')
        # cv2.destroyWindow('ADD-frame')

    def capture_video(self):
        # TBD
        pass


if __name__ == "__main__":
    recoder = ImgRec()
    recoder.capture_frame()
    

