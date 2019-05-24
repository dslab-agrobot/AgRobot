import time
import os


def mkdir(path):

	folder = os.path.exists(path)
	# create a folder if it does not exist and do nothing if it does
	if not folder:
		os.makedirs(path)
		print ("---  new folder.."+path+".  ---")
		print ("---  OK  ---")
 
	else:
		print ("---  There is this folder!  ---")

def cur_time():
	cur_time= time.strftime('%Y-%m-%d',time.localtime(time.time()))
	return cur_time

def rmdir(path):
	pass
pics_path='./'
print(cur_time())
mkdir(pics_path+cur_time())