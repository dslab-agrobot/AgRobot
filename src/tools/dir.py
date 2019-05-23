import time
import os

<<<<<<< HEAD
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
=======

def mkdir(path):

	folder = os.path.exists(path)
	# create a folder if it does not exist and do nothing if it does
	if not folder:
		os.makedirs(path)
>>>>>>> jiangxt
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