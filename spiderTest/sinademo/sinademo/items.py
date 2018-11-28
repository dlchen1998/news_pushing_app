# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinademoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class news(scrapy.Item):
    title = scrapy.Field()
    context = scrapy.Field()
    image = scrapy.Field()
