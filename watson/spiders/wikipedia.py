# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from watson.items import NuggetItem

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["http://en.wikipedia.org/"]
    start_urls = ["http://en.wikipedia.org/wiki/Data_structure",
                    "http://en.wikipedia.org/wiki/Array_data_structure",
                    "http://en.wikipedia.org/wiki/Record_(computer_science)",
                    "http://en.wikipedia.org/wiki/Associative_array",
                    "http://en.wikipedia.org/wiki/Hash_table",
                    "http://en.wikipedia.org/wiki/B-tree",
                    "http://en.wikipedia.org/wiki/Heap_(data_structure)",
                    "http://en.wikipedia.org/wiki/Binary_heap",
                    "http://en.wikipedia.org/wiki/Doubly_linked_list"
    ]

    rules = (
        #Rule(LinkExtractor(allow=(), restrict_xpaths=('/body//a')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for sel in response.xpath('//h1 | //h2 | //p | //pre'):
            item = NuggetItem()
            item['content'] = sel.extract()
            item['title'] = response.xpath('//title/text()').extract()
            yield item

    def parse_start_url(self, response):
        for sel in response.xpath('//h1 | //h2 | //p | //pre'):
                item = NuggetItem()
                item['content'] = sel.extract()
                item['title'] = response.xpath('//title/text()').extract()
                yield item