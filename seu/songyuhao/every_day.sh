#!/bin/bash
cd /home/ubuntu/seu/songyuhao;
/usr/bin/python3.6 dayReport.py >> /home/ubuntu/seu/songyuhao/log.txt
msg=$(tail -n 6  /home/ubuntu/seu/songyuhao/log.txt)
/usr/bin/python3.6 send_mail.py $msg
