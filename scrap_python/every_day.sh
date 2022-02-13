#!/bin/bash
path=$(cd $(dirname $0); pwd)
cd $path
/usr/bin/python3.6 scrap.py >> $path/log.txt
