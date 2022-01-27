import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from typing import ContextManager
import csv
import time

filename = "167974260.csv"
column =[]
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        column.append(row['QQ号']+"@qq.com")

if __name__ == '__main__':
    count=0
    while column:
        receiver=[]
        receiver.append(column.pop())
        print(receiver)
        