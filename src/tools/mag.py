import cv2

def Rot(frame, deg):
   width = frame.shape[1]
   height = frame.shape[0]
   M = cv2.getRotationMatrix2D((width/2,height/2),rot ,1)
   rot_frame = cv2.warpAffine(frame,M,(width,height))
   return rot_frame

def Zoom(frame, zoomSize):
   c_x = frame.shape[0]/2
   c_y = frame.shape[1]/2
   w_x = c_x/zoomSize
   w_y = c_y/zoomSize
   frame = frame[int(c_x-w_x):int(c_x + w_x), int(c_y-w_y):int(c_y+w_y)]
   frame = cv2.resize(frame,((int(frame.shape[1]*zoomSize)),
                             (int(frame.shape[0]*zoomSize))))
   return frame 

rot=0
zoom_factor=1.0
cap = cv2.VideoCapture(0)
# try setting to higher resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # set the Horizontal resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # Set the Vertical resolution
_ = cap.set(cv2.CAP_PROP_BRIGHTNESS,100)
_ = cap.set(cv2.CAP_PROP_SATURATION,50)
_ = cap.set(cv2.CAP_PROP_CONTRAST,35)
sat = 100
frame_count = 0

while(cap.isOpened()): 
   # setting some properties
   ret = cap.set(cv2.CAP_PROP_SATURATION,sat)
   # grab the frmae with grab/retrieve so we can connect multiple
   # cameras and get roughly synchronized imnages
   ret = cap.grab()
   ret, frame = cap.retrieve()
   # preprocess before storing
   rot_frame = Rot(frame, rot)
   zoom_frame = Zoom(rot_frame, zoom_factor)
   cv2.imshow('USB0-frame', zoom_frame)
   key = cv2.waitKey()
   if key != ord('q'):
      if key == ord('l'):
         rot += 2.5
      if key == ord('r'):
         rot -= 2.5
      if key == ord('i'):
         zoom_factor *= 1.05 if zoom_factor < 10.0 else 1.0
         print (zoom_factor)
      if key == ord('o'):
         zoom_factor *= (1.0/1.05) if zoom_factor > 1.0 else 1.0
         print (zoom_factor)
      if key == ord('+'):
         sat += 0.05 if sat < 1.0 else 0.0
      if key == ord('-'):
         sat -= 0.05 if sat > 0.0 else 0.0
      if key == ord('s'):
         cv2.imwrite("frame_base%d.jpg" % frame_count, zoom_frame)
         frame_count += 1
      continue
   else:
      break

cap.release()
cv2.destroyWindow('USB0-frame')
