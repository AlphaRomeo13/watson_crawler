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
    start_urls = [
                    "https://docs.oracle.com/javase/tutorial/getStarted/index.html",
                    "https://docs.oracle.com/javase/tutorial/java/index.html",
                    "https://docs.oracle.com/javase/tutorial/essential/index.html",
                    "https://docs.oracle.com/javase/tutorial/collections/index.html",
                    "https://docs.oracle.com/javase/tutorial/datetime/index.html",
                    "https://docs.oracle.com/javase/tutorial/deployment/index.html",
                    "https://docs.oracle.com/javase/tutorial/extra/certification/index.html",
                    "https://docs.oracle.com/javase/tutorial/uiswing/index.html",
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[contains(.,"Next")]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        scope = response.xpath('//*[@id="MainFlow"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        scope = response.xpath('//*[@id="MainFlow"]')
        for sel in scope.xpath('//h1 | .//h2 | .//h3 | .//h4 | .//p | .//ol | .//ul | .//pre'):
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item