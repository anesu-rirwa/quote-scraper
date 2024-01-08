# Quote Scraper

## Overview
This is a basic web scraper created using Scrapy to extract quotes from the website quotes.toscrape.com. The scraper is implemented as a Python class named QuoteSpider, which subclasses scrapy.Spider.

## Usage
To run the scraper, use the following command:

```bash
scrapy runspider scraper.py
```

This command will initiate the spider and start crawling the specified URL(s).

## Spider Details
### Spider Name
The spider is named quote-spider. You can change this name by modifying the name attribute in the QuoteSpider class.

```python
name = 'quote-spider'
```

### Starting URLs
The spider begins crawling from the URL `https://quotes.toscrape.com`. You can modify the start_urls attribute to start from different URLs.

```python
start_urls = ['https://quotes.toscrape.com']
```

## Data Extraction
The spider extracts the following information from each quote on the page:

Text: The text of the quote.
Author: The author of the quote.
About: A link to more information about the author.
Tags: Tags associated with the quote.

## Selectors
The CSS selectors used for data extraction are defined in the parse method:

```python
QUOTE_SELECTOR = '.quote'
TEXT_SELECTOR = '.text::text'
AUTHOR_SELECTOR = '.author::text'
ABOUT_SELECTOR = '.author + a::attr("href")'
TAGS_SELECTOR = '.tags > .tag::text'
NEXT_SELECTOR = '.next a::attr("href")'
```

Feel free to adjust these selectors based on the structure of the HTML elements on the website.

## Pagination
The spider also handles pagination by following the "Next" link on each page. The next page URL is extracted using the NEXT_SELECTOR. If there is a next page, the spider generates a new request to crawl that page.

```python
next_page = response.css(NEXT_SELECTOR).extract_first()
if next_page:
    yield scrapy.Request(
        response.urljoin(next_page),
    )
```

## Running the Spider
After making any modifications, run the scraper using the previously mentioned command to initiate the spider and start extracting quotes.

**Note: Make sure you have Scrapy installed before running the spider:

```bash
pip install scrapy
```

## Disclaimer
This scraper is meant for educational purposes only. Be sure to review and comply with the terms of service of any website you intend to scrape. Unauthorized scraping may violate website policies and legal regulations. Use this tool responsibly and ethically.
