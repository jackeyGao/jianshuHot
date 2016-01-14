# -*- coding: utf-8 -*-
'''
File Name: jianshu/linkextractor.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 三  1/ 6 11:20:37 2016
'''
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor


class DailyLinkExtractor(BaseSgmlLinkExtractor):


    def process_value(value):
        #m = re.search("javascript:goToPage\('(.*?)'", value)
        #if m:
        #    return m.group(1)
        return "http://www.baidu.com"
