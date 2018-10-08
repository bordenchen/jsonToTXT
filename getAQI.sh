#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin:$NCARG_ROOT/bin
export PATH

value=$(python3.6 ~/python_code/getAQI.py 2>&1) 
DATE=`date +%Y-%m-%d-%H-%M`
echo "${value} ServerTime: ${DATE}" 
