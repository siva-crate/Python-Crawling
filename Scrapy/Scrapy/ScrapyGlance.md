## Scrapy at a glance (crawling and scraping useful)

> Scrapy (/ˈskreɪpaɪ/) is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

> general purpose : web crawling , designed for web scraping.

## Walk-through of an example spider

> 

      import scrapy

      class QuotesSpider(scrapy.Spider):
      name = "quotes"
      start_urls = [
            "https://quotes.toscrape.com/tag/humor/",
      ]

      def parse(self, response): # Auto Call by itself
            for quote in response.css("div.quote"):
                  yield {
                  "author": quote.xpath("span/small/text()").get(),
                  "text": quote.css("span.text::text").get(),
                  }

            next_page = response.css('li.next a::attr("href")').get()
            if next_page is not None:
                  yield response.follow(next_page, self.parse)

Put this in a text file, name it something like quotes_spider.py and run the spider using the runspider command:

> scrapy runspider quotes_spider.py -o quotes.jsonl

## What just happened?
      when application runs, Scrapy looked for a spider def and ran it thorugh it's crawler engine. started by making requests (defined in start_URL's) and called default callback method " parse " look for a link to the next page and schedule another request using same parse method as callback.

      > MAIN ADVANTAGES OF SCRAPY
            ..> req are scheduled and processed asynchronously
            ..> Note: other request keep going even if one fails or error occurs while handl
            ..> enables fast carwls,
            ..> You can do things like setting a download delay between each request, limiting the amount of concurrent requests per domain or per IP, and even using an auto-throttling extension that tries to figure these settings out automatically.

## what else?
> Built-in support for selecting and extracting data from HTML/XML sources using extended CSS selectors and XPath expressions, with helper methods for extraction using regular expressions.

> Built-in support for generating feed exports in multiple formats (JSON, CSV, XML) and storing them in multiple backends (FTP, S3, local filesystem)

> Robust encoding support and auto-detection, for dealing with foreign, non-standard and broken encoding declarations.

> Strong extensibility support, allowing you to plug in your own functionality using signals and a well-defined API (middlewares, extensions, and pipelines).

> A wide range of built-in extensions and middlewares for handling:

    cookies and session handling

    HTTP features like compression, authentication, caching

    user-agent spoofing

    robots.txt

    crawl depth restriction

    and more


> A Telnet console for hooking into a Python console running inside your Scrapy process, to introspect and debug your crawler

> Plus other goodies like reusable spiders to crawl sites from Sitemaps and XML/CSV feeds, a media pipeline for automatically downloading images (or any other media) associated with the scraped items, a caching DNS resolver, and much more!
