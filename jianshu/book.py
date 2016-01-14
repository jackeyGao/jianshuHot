# -*- coding: utf-8 -*-
'''
File Name: jianshu/book.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 三  1/ 6 15:37:06 2016
'''
import sys
import datetime
import commands
from jianshu.db import Note

reload(sys)
sys.setdefaultencoding('utf-8')

def export_to_markdown(item):
    with open('output/markdown/%s.md' % item.slug, 'w') as f:
        page_header = '# **%s**\n' % item.title
        page_header += '> %s view\n' % item.views_count
        page_header += '> %s\n\n' % item.url
        f.write(page_header + item.content)


def write_readme():
    content = ''
    content += '简书热门\n'
    content += '========\n\n'
    content += '生成时间: %s\n' % datetime.datetime.now()
    with open('output/README.md', 'w') as f:
        f.write(content)


def write_summary():
    content = '* [Jianshu Hot](markdown/README.md)\n'

    for i in Note.select().order_by(Note.views_count.desc()).execute():
        content += ' - [%s](markdown/%s.md)\n' % (i.title, i.slug)

    with open('output/SUMMARY.md', 'w') as f:
        f.write(content)

def gen_book():
    return commands.getstatusoutput('soruce /etc/profile; cd output/; gitbook mobi')


def gen_markdown():
    write_readme()
    write_summary()
    for item in Note.select().execute():
        export_to_markdown(item)

