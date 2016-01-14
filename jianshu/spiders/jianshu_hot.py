# -*- coding: utf-8 -*-
import json
import scrapy
import html2text
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import BaseSgmlLinkExtractor
from jianshu.items import JianshuItem
from jianshu.items import JianshuImageItem


class JianshuHotSpider(CrawlSpider):
    name = "jianshu_hot"
    allowed_domains = ["jianshu.com"]
    start_urls = (
        'http://www.jianshu.com/',
    )

    rules = (
        Rule(LinkExtractor(
                    allow=(r'http://www.jianshu.com/p/\w+',)
                ), 
                callback='parse_item',
            ), 

        #Rule(BaseSgmlLinkExtractor(
        #        tag="button",
        #        attr="data-url"
        #        ),
        #    callback="parse_item_url",
        #    follow=True
        #    ),
    )
    def parse_item_url(self, response):
        pass

    def parse_item(self, response):
        title = response.xpath('//h1[@class="title"]/text()').extract()[0]
        body = response.xpath('//div[@class="show-content"]').extract()[0]
        attr = response.xpath('//script[@data-name="note"]/text()').extract()
        images = response.xpath('//div[@class="image-package"]/img/@src').extract()
        notes = json.loads(attr[0].strip())

        # 生成markdown 内容
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.inline_links = False
        content = h.handle(body)

        item = JianshuItem()
        item["title"] = title
        item["content"] = content.replace('-\n', '-').replace('\n?', '?')
        item["url"] = notes['url']
        item["slug"] = notes['slug']
        item["views_count"] = notes['views_count']
        item["likes_count"] = notes['likes_count']
        item["images"] = images
        yield item

