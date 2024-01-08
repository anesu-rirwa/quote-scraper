# create a basic scraper that uses Scrapy as its foundation

# create a python class that subclasses scrapy.Spider

import scrapy # to use the classes the package provides

class QuoteSpider(scrapy.Spider):
    name = 'quote-spider' # name for the spider
    start_urls = ['https://quotes.toscrape.com'] # a list of URls that you start to crawl from

    # to test the scraper enter the following code
    # scrapy runspider scraper.py

    # Extracting Data from a Page
    # first we grab each quote by looking for the parts of the page that have the data we want
    # for each quote, grab the data we want by pulling the data out of the HTML tags

    def parse(self, response):
        QUOTE_SELECTOR = '.quote'
        TEXT_SELECTOR ='.text::text'
        AUTHOR_SELECTOR = '.author::text'

        for quote in response.css(QUOTE_SELECTOR):
            pass


