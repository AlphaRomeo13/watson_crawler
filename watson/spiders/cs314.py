# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class cs314Spider(CrawlSpider):
    name = "cs314"
    allowed_domains = ["www.cs.utexas.edu"]
    start_urls = ["http://www.cs.utexas.edu/users/novak/cs31411.html"]

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