import scrapy
from scrapy.http import FormRequest

from scrapy.utils.response import open_in_browser


class ItemsSpider(scrapy.Spider):
    name = "items"

    start_urls = ['https://intrahard.com/login',]


    def parse(self, response):    
        return FormRequest.from_response(response, 
                                        formdata={                                                 
                                                'usuario':'urssmorris@gmail.com', 
                                                'pwd':'elgranKathogas3',
                                                'login':'1'}, 
                                        callback=self.scrape_pages)
    
    def parse(self, response):
        open_in_browser(response)


        self.logger.info("first spider")
        items = response.css('div.item d-flex flex-column justify-content-between w-100')
        for item in items:
            yield {
                'item': item.css('.h3::text').get(),
                'precio': item.css('.mb-0::text').get(),
            }