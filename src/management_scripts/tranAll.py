"""
transfer photos to server per day by scp


__copyright__=""
__email__ = ""
__license__ = "GPL V3"
__version__ = "0.1"


Use this script by :
```
$ chmod +x absPath/tranAll.py    # make this script run-able
$ crontab -e                    # write these cmd in

30 8 * * * python absPath/tranAll.py     # run 8:30 per day
# add some more daily running
```


------------------------------------------------------------
ATTENTION PLEASE

You need set up the cameras as wrote in src/tools/ai/imgRec.py
Edit crontab with 'crontab -e' as below, then it can be executed automatic
------------------------------------------------------------

"""