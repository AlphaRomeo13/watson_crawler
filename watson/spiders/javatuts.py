# -*- coding: utf-8 -*-

# use this command to run:
# scrapy crawler javatuts -o items.json

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class JavatutsSpider(CrawlSpider):
    name = "javatuts"
    allowed_domains = ["docs.oracle.com"]
    start_urls = ["http://docs.oracle.com/javase/tutorial/deployment/index.html"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[contains(.,"Next")]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for sel in response.xpath('//h1 | //h2 | //p | //pre | //ul | //ol'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        for sel in response.xpath('//h1 | //h2 | //p | //pre | //ul | //ol'):
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item