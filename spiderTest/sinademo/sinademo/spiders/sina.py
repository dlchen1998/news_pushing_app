import scrapy
from sinademo.items import news


class sinaspide(scrapy.spiders.CrawlSpider):
    name = "sina"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = news()
            item['title'] = each_movie.xpath('./h5/a/@title').extract()[0]

            yield item

