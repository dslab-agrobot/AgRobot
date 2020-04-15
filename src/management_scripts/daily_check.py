# -*-encoding=utf8-*-
"""
sending emails to Jiang and Wei every day


__copyright__="Weiyq"
__email__ = "wyq_l@qq.com"
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```
$ chmod +x absPath/daily_check.py    # make this script run-able
$ crontab -e                    # write these cmd in

30 8 * * * python3 /home/pi/AgRobot/src/management_scripts/daily_check.py     # run 8:30 per day
# add some more daily running
```


------------------------------------------------------------
ATTENTION PLEASE

Edit crontab with 'crontab -e' as below, then it can be executed automatic
------------------------------------------------------------

"""

import sys,os,time
sys.path.append("/home/pi/AgRobot/src/")
from tools import send_email

title='I am fine'
content='I am pi from HuYang building ,I am alive.'
address=['17611039236@163.com','zhouqg@lzu.edu.cn','jiangxt18@lzu.edu.cn','weiyq18@lzu.edu.cn']
send_email(title,content,address)


