# -*- coding: utf-8 -*-
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from typing import ContextManager
import csv
import time
#from requestsAndBs4 import get_content

#import socks
#import socket
#socks.set_default_proxy(socks.HTTP,"127.0.0.1", 10808)
#socket.socket = socks.socksocket

filename = "167974260.csv"
column =[]
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        column.append(row['QQ号']+"@qq.com")
        
#print(column)
    
mailHost = 'smtp.163.com'
mailPort = 465

users=['kaoyantiaojipro@163.com','kaoyantiaojipro6@163.com','kaoyantiaojipro2@163.com']
passws = ['CMVQUFTGGQMXCSXW','OYTUPHFDKUDTTDIK','XERFQGKZNMYNQNCI']
#os.environ.get("ZVENGRMQAKMXXYUC")
# passw_lxf = os.environ.get("lixiangfu@146")

def sendMail(receiver,count):
    user_lxf=users[count%3]
    passw_lxf=passws[count%3]
    smptp = smtplib.SMTP_SSL(mailHost,mailPort)
    smptp.login(user=user_lxf,password=passw_lxf)

    msg = MIMEMultipart()

    msg['Subject']=Header("欢迎加入2022考研调剂群：959578208",'utf-8')
    msg['from']=user_lxf
    msg['to']=','.join(receiver)
    
    content="里面有学长专门负责大家的复试，调剂答疑和指导。因为自己调剂的经历，这两年也帮助了一些身边的同学和学弟学妹做调剂，效果还不错。自己经历过那段焦虑的日子，所以我知道信息的珍贵，一个月内必须搜集大量零散信息非常累人。我一直想帮助更多也在纠结调剂的学弟学妹，也算我个人的创业小尝试吧。如果你愿意和我们交流的话，欢迎加入22年考研调剂群 959578208 里面有好几个学长在群里互动。复试、调剂答疑都欢迎交流，我们会努力提供你想要的信息。"
    #print(content)
    msg_content=MIMEText(content,'plain','utf-8')
    msg.attach(msg_content)

    smptp.sendmail(user_lxf,receiver,msg.as_string())

if __name__ == '__main__':
    count=0
    while column:
        receiver=[]
        receiver.append(column.pop())
        print(receiver)
        time.sleep(30)
        sendMail(receiver,count)
        count=count+1

