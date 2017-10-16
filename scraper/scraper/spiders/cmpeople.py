# -*- coding: utf-8 -*-
import scrapy


class CmpeopleSpider(scrapy.Spider):
    name = 'cmpeople'
    allowed_domains = ['creativemornings.com']
    start_urls = ['http://creativemornings.com/']

    def parse(self, response):
        pass
