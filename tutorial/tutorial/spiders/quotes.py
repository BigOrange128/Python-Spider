# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = TutorialItem()
            item['text'] = quote.css('.text::text').extract_first()     #选择e_f列表里的第一个
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)   #将相对url构造成绝对url
        yield scrapy.Request(url = url, callback = self.parse)   #构造新请求



