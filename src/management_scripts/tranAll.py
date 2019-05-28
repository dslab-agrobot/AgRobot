"""
transfer photos to server per day by scp


__copyright__="Weiyq"
__email__ = "wyq_l@qq.com"
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```
$ chmod +x absPath/tranAll.py    # make this script run-able
$ crontab -e                    # write these cmd in

30 23 * * * python3 /home/pi/AgRobot/src/management_scripts/tranAll.py     # run 23:30 per day
# add some more daily running
```


------------------------------------------------------------
ATTENTION PLEASE

You need set up the cameras as wrote in src/tools/ai/imgRec.py
Edit crontab with 'crontab -e' as below, then it can be executed automatic
------------------------------------------------------------

"""
import sys,os,time
sys.path.append("/home/pi/AgRobot/src/tools")
from tools import dir

base_path='/home/pi/AgRobot/src/management_scripts/'
cur_time=dir.cur_time()
path = base_path+cur_time

agro_server='root@178.128.126.229'
remote_dir='/home/AgRobot/pics/'
cmd ='scp -r '+path +' '+agro_server+':'+remote_dir
os.system(cmd)``
