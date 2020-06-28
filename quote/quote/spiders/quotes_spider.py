import scrapy
from ..items import QuoteItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username':'vinay',
            'password': 'hello'
        },callback=self.start_scraping)

    def start_scraping(self, response):
        # we can look in console for response 302 or in browser with open_in_browser
        # to know whether the login action occured
        # this method automatically open the browser with logged in.
        open_in_browser(response)

        # ceating Item instance
        items = QuoteItem()

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
