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
        ABOUT_SELECTOR = '.author + a::attr("href")'
        TAGS_SELECTOR = '.tags > .tag::text'
        NEXT_SELECTOR = '.next a::attr("href")'

        for quote in response.css(QUOTE_SELECTOR):
            yield {
                'text': quote.css(TEXT_SELECTOR).extract_first(),
                'author': quote.css(AUTHOR_SELECTOR).extract_first(),
                'about': 'https://quotes.toscrape.com' + quote.css(ABOUT_SELECTOR).extract_first(),
                'tags': quote.css(TAGS_SELECTOR).extract(),
            
            }

        next_page = response.css(NEXT_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
            )



