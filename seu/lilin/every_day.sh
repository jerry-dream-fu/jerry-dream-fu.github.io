#!/bin/bash
cd /home/ubuntu/seu/lilin;
/usr/bin/python3.6 dayReport.py >> /home/ubuntu/seu/lilin/log.txt
msg=$(tail -n 6  /home/ubuntu/seu/lilin/log.txt)
/usr/bin/python3.6 send_mail.py $msg
