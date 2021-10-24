# -*- coding: utf-8 -*-
import scrapy


class TacSpider(scrapy.Spider):
    name = 'TAC'
    allowed_domains = ['county.org']
    start_urls = ['https://www.county.org/About-Texas-Counties/Texas-County-Websites']

    def parse(self, response):
        return {'county': response.css('.large-15 a::text').get(),
                'Link': response.css('.large-15 a').attrib['href']}
