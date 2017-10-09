# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class IpsItem(Item):
    ip_address = Field()
    port = Field()
    type = Field()
    anonymity_flag = Field()
    server_place = Field()
