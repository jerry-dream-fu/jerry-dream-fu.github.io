#!/bin/bash
path=$(pwd)
cd $path
/usr/bin/python3.6 scrap.py >> $path/log.txt
