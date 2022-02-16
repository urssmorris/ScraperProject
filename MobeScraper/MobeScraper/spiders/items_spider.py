from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.http.request import Request


class ItemsSpider(Spider):
    name = 'items'
    start_urls = ['https://www.gitextranet.com.ar/login']
    handle_httpstatus_list = [403]
    # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    # def start_requests(self):
    #     headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    #     for url in self.start_urls:
    #         yield Request(url, headers=headers)

    def parse(self, response):
        yield FormRequest(url=self.start_urls[0],
                                        formdata= {
                                        'user_name':"GOETTEMR",
                                        'password':"elgranKathogas3",
                                        'login':"Ingresar"
                                        }, 
                                        callback=self.scrape_ftse)
        


    def scrape_ftse(self, response):
        print("logged in!")
        
        yield{ 'tipo_precio' : response.css('div.tipo_precio').get() }

        # items = response.css('div.tipo_precio')
        # for item in items:
        #     yield {
        #         'item': item.css('.exportar::text').get()
        #     }


        