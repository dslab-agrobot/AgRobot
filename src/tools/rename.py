import sys,os

m_path ='./agri_robot_picture/'

for dirpath,folders,filenames in os.walk(m_path):
    break

for folder in folders:
    cnt = 0
    f_contain = "".join(folder.split('-')[:])
    for dirpath,folders,filenames in os.walk(m_path+ folder):
        break
    for f in filenames:
        n_name = 'IMG-'+f_contain+'-'+str(cnt)+'.'+f.split('.')[-1]
        if n_name not in filenames :
            os.rename(m_path+'/'+folder+'/'+f,m_path+'/'+folder+'/'+n_name)
        cnt += 1
    
