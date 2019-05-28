#coding=utf-8
import os
import time
import serial


def __init(name=None):
    if name is None:
        dev = os.popen("ls -l /dev/ttyACM* | awk '{print $10}'")
    else:
        dev = os.popen("ls -l /dev/ttyUSB* | awk '{print $10}'")
    dev = dev.readline().strip()
    ser = None
    try:
        ser = serial.Serial(dev, 115200, timeout=3)
        time.sleep(2)
    except Exception as e:
        print ('[Error] Failed to connect arduino. Reason:', e)
        if ser:
            ser.close()
            ser = serial.Serial(dev, 115200, timeout=16)
    finally:
        pass
    return ser


def send_msg(msg, name = None):
    ser = __init(name)
    for i in range(100):
        try:
            print(i)
            time.sleep(1)
            ser.write(msg)
            break
        except Exception as e:
            print("ser write msg error", e)
            if ser:
               ser.close()
               ser = __init()
        finally:
            pass
    msg = None
    for i in range(100):
        try:
            msg = ser.read_until('!!!')
            break 
        except Exception as e:
            print("ser read msg error", e)
            if ser:
                ser.close()
                ser = __init()
        finally:
            pass
    if ser:
        ser.close()
    return msg


if __name__ == '__main__':
    print (send_msg('X+0043;'))
