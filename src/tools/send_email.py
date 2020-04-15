# coding: utf-8
"""
send email using 17611039236@163.com
__copyright__="Weiyq"
__email__ = "<wyq_l@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


```
Use this script by :
```
from send_email import send_email
#email title   
title='title warning from huyang!!!!'
#email content 
content='please come to huyang building  camera is down， check out cameras!'
#send to list 
address=['17611039236@163.com','wyq_l@qq.com','weiyq18@lzu.edu.cn']
send_email(title,content,address)

```

"""
import smtplib
from email.mime.text import MIMEText
from time import sleep

#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com'  
#163用户名
mail_user = '17611039236'  
#密码(部分邮箱为授权码) 网易为授权码
mail_pass = 'weiyq18'   
# mail_pass = 'nopasswd@dslab'   
#邮件发送方邮箱地址
sender = '17611039236@163.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['wyq_l@qq.com','weiyq18@lzu.edu.cn']  

#设置email信息
#邮件内容设置
def email_message(title,content,address_list):
    email_content=content
    email_title=title
    message = MIMEText(email_content,'plain','utf-8')
    #发送方信息
    message['From'] = "{}".format(sender)
    #接受方信息     
    message['To'] = ",".join(address_list)
    #邮件title
    message['Subject'] = email_title
    return message

def send_email(title,content,to_address):
    
    for i in range(100)
        try:
            smtpObj = smtplib.SMTP() 
            #连接到服务器
            smtpObj.connect(mail_host,25)
            print('connecting 163 server')
            #登录到服务器
            smtpObj.login(mail_user,mail_pass)
            print('logining into mail_user') 
            #发送
            message=email_message(title,content,to_address)
            print('sending message')
            smtpObj.sendmail(
                sender,to_address,message.as_string()) 
            #退出
            smtpObj.quit() 
            print('success')
            break
        except smtplib.SMTPException as e:
            print('error',e) #打印错误

if __name__ == "__main__":
    title='title warning from huyang test!!!'
    content='p '
    address=['17611039236@163.com','agrobot@irc.dslab.cf','weiyq18@lzu.edu.cn']
    send_email(title,content,address)
