# -*-encoding=utf-8-*-
"""
Navigator to control robot to move and act


__copyright__="Liuxin","Jiangxt"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.2"


Use ths script by:
```
from connector import send_msg

# Use send_msg with implicit name means to send to 'move'
send_msg('X+0043;')
send_msg('Y+028;')

```


"""
import os
import time
import serial

MAX_RETRY = 10


def __init(name=None):
    if name is None:
        dev = os.popen("ls -l /dev/ttyACM* | awk '{print $10}'")
    else:
        dev = os.popen("ls -l /dev/ttyUSB* | awk '{print $10}'")
    dev = dev.readline().strip()
    ser = None

    # We can't find this device sometimes , so having some retry can fix it
    for cnt in range(MAX_RETRY):
        try:
            cnt += 1
            ser = serial.Serial(dev, 115200, timeout=3)

            # We need this sleep for reacting
            time.sleep(2)
            break
        except Exception as e:
            print('\r\n [Error] Failed to connect arduino. Reason:', e)
            if cnt < MAX_RETRY:
                print('Retrying connecting [%d]')
        finally:
            if ser:
                ser.close()

    return ser


def send_msg(msg, name=None):
    ser = __init(name)
    cnt = 0
    try:
        cnt += 1
        time.sleep(1)
        ser.write(msg)
    except Exception as e:
        print("\r\n [Error] Failed to send message. Reason:", e)
        if cnt < MAX_RETRY:
            print('Try to create a new connection')
    finally:
        if ser:
            ser.close()
            ser = __init()

    msg = None
    try:
        msg = ser.read_until('!!!')
    except Exception as e:
        print("[Error] Failed to send message. Reason: %s \n"
              "Useless for retrying to read or create new one", e)
    finally:
        if ser:
            ser.close()
            ser = __init()

    if ser:
        ser.close()
    return msg


if __name__ == '__main__':
    print(send_msg('X+0043;'))

"""
Indeed , there are still two problems rarely happen [ occurs less than 5% ],
and we have no good idea for these 
    1) Electronic interference or something else may influence the sending
        of serial port . It means we send all part of message but device just
        receive part of them . [Y moves wried distance twice with correct cmd and
        correct return]
    
    2) Arduino just return its message once without confirmation . So sometimes we
        can't read message that can do nothing but raise a error. (Retrying to read
        message from serial port is stupid . )
"""
