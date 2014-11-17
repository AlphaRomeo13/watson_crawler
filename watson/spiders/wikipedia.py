# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
                    "http://en.wikipedia.org/wiki/Abstract_data_type",
                    "http://en.wikipedia.org/wiki/Linked_list"
    ]

    rules = (
        #Rule(LinkExtractor(allow=(r'(.*?computer_science\)$)|(.*?abstract_data_type\)$)|(.*?_programming\)$)|(.*?_programming$)'), restrict_xpaths=('//*[@id="mw-content-text"]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        scope = response.xpath('//*[@id="mw-content-text"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        scope = response.xpath('//*[@id="mw-content-text"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):   # use: '//h2[1]/preceding-sibling::p' to get intro paragraphs
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item