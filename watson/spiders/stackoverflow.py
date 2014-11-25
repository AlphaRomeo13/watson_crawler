# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class StackoverflowSpider(CrawlSpider):
    name = "stackoverflow"
    download_delay = 0.5
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
                    # "http://stackoverflow.com/questions/tagged/android",
                    "http://stackoverflow.com/questions/tagged/java",
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'android|java'), restrict_xpaths=('//*[@id="questions"]')), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[contains(.,"next")]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        scope = response.xpath('//*[@itemprop="acceptedAnswer"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        scope = response.xpath('//*[@itemprop="acceptedAnswer"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):   # use: '//h2[1]/preceding-sibling::p' to get intro paragraphs
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item