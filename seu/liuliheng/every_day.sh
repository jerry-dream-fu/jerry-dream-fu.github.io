#!/bin/bash
cd /home/ubuntu/seu/liuliheng;
/usr/bin/python3.6 dayReport.py >> /home/ubuntu/seu/liuliheng/log.txt
msg=$(tail -n 6  /home/ubuntu/seu/liuliheng/log.txt)
/usr/bin/python3.6 send_mail.py $msg
