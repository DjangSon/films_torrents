# -*- coding: UTF-8 -*-
from scrapy import spider
from ips.items import IpsItem


class KuaiSpider(spider.Spider):
    name = 'kuai'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/outha/1/']

    def parse(self, response):
        for tr in response.xpath('//table/tbody/tr'):
            item = IpsItem()
            item['ip_address'] = tr.xpath(u'.//td[@data-title="IP"]/text()').extract()
            item['port'] = tr.xpath(u'.//td[@data-title="PORT"]/text()').extract()
            item['type'] = tr.xpath(u'.//td[@data-title="类型"]/text()').extract()
            item['anonymity_flag'] = tr.xpath(u'.//td[@data-title="匿名度"]/text()').extract()
            item['server_place'] = tr.xpath(u'.//td[@data-title="位置"]/text()').extract()
            yield item
