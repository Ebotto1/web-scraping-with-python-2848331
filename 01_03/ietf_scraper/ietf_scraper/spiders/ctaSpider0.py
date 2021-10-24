import scrapy


class CtaspiderSpider(scrapy.Spider):
    name = 'ctaSpider'
    allowed_domains = ['county.org']
    start_urls = ['https://www.county.org/About-Texas-Counties/Texas-County-Websites/']

    def parse(self, response):
        return {'county': response.css('.large-15 a::text').get(),
                'Link': response.css('.large-15 a').attrib['href']}

#scrapy startproject ctaspider <website>
#scrapy genspider
#scrapy runspider ctaSpider.py -o cta_out.json -t json
