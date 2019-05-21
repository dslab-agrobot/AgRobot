#coding=utf-8
import os
import time
import serial


class RpiArdConnector:
    def __init__(self):
        # dev = os.popen("ls -l /dev/ttyACM* | awk '{print $10}'")
        # self.dev = dev.readline().strip()
        self.dev='/dev/ttyACM0'
        self.ser = None
        # dev.close()

    def connect(self):
        try:
            self.ser = serial.Serial(self.dev, 115200, timeout=3)
            time.sleep(2)
            return True
        except Exception as e:
            print ('[Error] Failed to connect arduino. Reason:', e)
            return False

    def send_msg(self, msg):
        if not self.ser:
            if not self.connect():
              return None
        for i in range(100):
            try:
                print(i)
                time.sleep(0.1)
                self.ser.write(msg)
                break
            except(Exception):
                print("ser write msg error")
            finally:
                pass
        msg=None 
        for i in range(100):
            try:
                msg=self.ser.read_until('!!!')
                break 
            except(Exception):
                print("ser read msg error")
            finally:
                pass
        return msg
    
    def disconnect(self):
        if self.ser:
            self.ser.close()


if __name__ == '__main__':
    connector = RpiArdConnector() 
    print (connector.send_msg('X+0043;'))
