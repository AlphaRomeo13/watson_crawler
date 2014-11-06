# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

from scrapy.exceptions import DropItem
from scrapy.contrib.exporter import JsonItemExporter

class CleanHTMLPipeline(object):

    # words_to_filter = ['<h2>navigation menu</h2>', '<h2>see also</h2>', '<h2>See also</h2>', '<h2>references</h2>', '<h2>References</h2>',]

    def process_item(self, item, spider):
        itemString = unicode(item['content'])

        # for word in self.words_to_filter:
        #    if word in itemString.lower():
        #       raise DropItem("Contains forbidden word: %s" % word)

        itemString = re.sub(r'<span(.*?)>', '', itemString)
        itemString = re.sub(r'</span>', '', itemString)
        itemString = re.sub(r'<a(.*?)>', '', itemString)
        itemString = re.sub(r'</a>', '', itemString)
        itemString = re.sub(r'<sup(.*?)>', '', itemString)
        itemString = re.sub(r'</sup>', '', itemString)
        itemString = re.sub(r'<img(.*?)>', '', itemString)
        itemString = re.sub(r'\[.*?\]', '', itemString)
        itemString = itemString.replace('<i>', '').replace('</i>', '')
        itemString = itemString.replace('<code>', '<strong>').replace('</code>', '</strong>')
        itemString = re.sub(r'<code(.*?)>', '<strong>', itemString)
        itemString = itemString.replace('<pre>', '<p><i>').replace('</pre>', '</i></p>')
        itemString = re.sub(r'<pre(.*?)>', '<p><i>', itemString)
        item['content'] = itemString
        
        return item

class JSONExportPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'w')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

