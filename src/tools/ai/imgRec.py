"""
Capture img from two camera and join them for Agrobot


__copyright__="Jiangxt; Zhip"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```

```



------------------------------------------------------------
ATTENTION PLEASE

You need to plug the two camera with order in a raspberry-pi
due to open-cv made default index when it pluged.

Make Sure the FIRST one that be plugged should be the
HIGHT RESOLUTION one .
------------------------------------------------------------
"""

import cv2
import datetime


class ImgRec(object):
    """Image-Recoder for grapping imgs from two cameras

    
    **** how to use or something ****


    Attributes:
        **** tbd ****

    """

    def __init__(self):
        self.cap_h = cv2.VideoCapture(0)
        self.cap_l = cv2.VideoCapture(1)
        
        # Try setting to higher resolution
        self.cap_h.set(cv2.CAP_PROP_FRAME_WIDTH,1280) # set the Horizontal resolution
        self.cap_h.set(cv2.CAP_PROP_FRAME_HEIGHT,720) # Set the Vertical resolution
        self.cap_l.set(cv2.CAP_PROP_FRAME_WIDTH,640) # set the Horizontal resolution
        self.cap_l.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # Set the Vertical resolution
        
        # Try setting to better effect of camera with hight resolution
        self.cap_h.set(cv2.CAP_PROP_BRIGHTNESS,100)
        self.cap_h.set(cv2.CAP_PROP_SATURATION,100)
        self.cap_h.set(cv2.CAP_PROP_CONTRAST,30)

        # Try setting to better effect of camera with low resolution
        self.cap_l.set(cv2.CAP_PROP_BRIGHTNESS,0)
        self.cap_l.set(cv2.CAP_PROP_SATURATION,50)
        self.cap_l.set(cv2.CAP_PROP_CONTRAST,35)

    def __del__(self):
        self.cap_h.release()
        self.cap_l.release()
    
    def capture_frame(self):

        if not (self.cap_l.isOpened()and self.cap_h.isOpened()):
            return False
        
        # grab the frmae with grab/retrieve so we can connect multiple
        # cameras and get roughly synchronized imnages
        ret_h = self.cap_h.grab()
        ret_h, frame_h = self.cap_h.retrieve()
        ret_l = self.cap_l.grab()
        ret_l, frame_l = self.cap_l.retrieve()

        # name the photo by date and time that we can make it easier for 
        # recording and sorting
        now_time = datetime.datetime.now()
        time_string = now_time.strftime("%Y%m%d_%H:%M:%S")
        
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
        cv2.imwrite(time_string + ".jpg", frame_h)
        
        # delete rets and frames
        del ret_h,ret_l,frame_h,frame_l
        
        # do not forget to destroy windows after showing them
        # cv2.destroyWindow('USB0-frame')
        # cv2.destroyWindow('USB1-frame')
        # cv2.destroyWindow('ADD-frame')

    def capture_video(self):
        # TBD
        pass
