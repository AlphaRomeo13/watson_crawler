# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class AndroidSpider(CrawlSpider):
    name = "android"
    allowed_domains = ["developer.android.com"]
    start_urls = [                
                    "https://developer.android.com/guide/index.html",
    ]

    rules = (
        Rule(LinkExtractor(allow=('guide'), restrict_xpaths=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        scope = response.xpath('//*[@id="jd-content"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        scope = response.xpath('//*[@id="jd-content"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item