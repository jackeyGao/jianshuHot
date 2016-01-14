#!/bin/bash
# File Name: init.sh
# Author: JackeyGao
# mail: junqi.gao@shuyun.com
# Created Time: 一  1/11 13:38:04 2016


cd $(dirname $0)
python -c "from jianshu.db import init_table; init_table()"

mkdir -p output/markdown 
mkdir -p output/images
mkdir -p output/books

touch output/README.md
touch output/SUMMARY.md

echo "[INFO] 完成"
