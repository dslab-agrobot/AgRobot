#coding=utf-8
import os
import time
import serial


def __init(name):
    if name is None:
        dev = os.popen("ls -l /dev/ttyACM* | awk '{print $10}'")
    else:
        dev = os.popen("ls -l /dev/ttyUSB* | awk '{print $10}'")
    dev = dev.readline().strip()
    ser = None
    dev.close()
    try:
        ser = serial.Serial(dev, 115200, timeout=3)
        time.sleep(2)
    except Exception as e:
        print ('[Error] Failed to connect arduino. Reason:', e)
    return ser


def send_msg(msg, name = None):
    ser = __init(name)
    for i in range(100):
        try:
            print(i)
            time.sleep(0.1)
            ser.write(msg)
            break
        except Exception:
            print("ser write msg error")
        finally:
            pass
    msg = None
    for i in range(100):
        try:
            msg = ser.read_until('!!!')
            break 
        except Exception:
            print("ser read msg error")
        finally:
            pass
    if ser:
        ser.close()
    return msg


if __name__ == '__main__':
    print (send_msg('X+0043;'))
