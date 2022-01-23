# -*- coding: utf-8 -*-
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from typing import ContextManager

#from requestsAndBs4 import get_content

mailHost = 'smtp.163.com'
mailPort = 465

user_lxf='lxf1632046131@163.com'
passw_lxf = 'ZVENGRMQAKMXXYUC'
#os.environ.get("ZVENGRMQAKMXXYUC")
# passw_lxf = os.environ.get("lixiangfu@146")

def sendMail():
    receiver=['18292887300@163.com']
    smptp = smtplib.SMTP_SSL(mailHost,mailPort)
    smptp.login(user=user_lxf,password=passw_lxf)

    msg = MIMEMultipart()

    msg['Subject']=Header("每日健康打卡",'utf-8')
    msg['from']=user_lxf
    msg['to']=','.join(receiver)
    
    content=sys.argv[1]+' '+sys.argv[23]
    #print(content)
    msg_content=MIMEText(content,'plain','utf-8')
    msg.attach(msg_content)

    smptp.sendmail(user_lxf,receiver,msg.as_string())

if __name__ == '__main__':
    sendMail()
