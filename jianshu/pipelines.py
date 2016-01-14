# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from peewee import *
from jianshu.settings import BLOCK_LIST
from jianshu.image import get_image_name
from jianshu.db import Note
from jianshu.db import Image
reload(sys)
sys.setdefaultencoding('utf-8')

class JianshuPipeline(object):
    def process_item(self, item, spider):
        if item["slug"] in BLOCK_LIST:
            return item

        # replace image url
        print(u"抓取完毕: %s" % item["title"])
        content = item["content"]
        for img in item["images"]:
            path = get_image_name(img)
            Image.insert(
                    slug=item["slug"],
                    url=img,
                    path=path
                    ).execute()
            content = content.replace(img, '../images/%s' % path)

        try:
            Note.insert(
                title = item["title"],
                slug = item["slug"],
                url = item["url"],
                content = content,
                likes_count = int(item["likes_count"]),
                views_count = int(item["views_count"])
                ).execute()

        except IntegrityError as e:
            logger.warn('%s SKIP E: (%s)' % (dict(item), str(e)))

        return item
