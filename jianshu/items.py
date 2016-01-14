# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    slug = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    likes_count = scrapy.Field()
    views_count = scrapy.Field()
    images = scrapy.Field()


class JianshuUrlItem(scrapy.Item):
    url = scrapy.Field()

class JianshuImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
