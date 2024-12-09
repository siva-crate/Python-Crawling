## This tutorial will walk you through these tasks:

    Creating a new Scrapy project

    Writing a spider to crawl a site and extract data

    Exporting the scraped data using the command line

    Changing spider to recursively follow links

    Using spider arguments

>> scrapy startproject tutorial (creating a project) & directory like below


tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

## Our first spider

>> Spiders are classes that you define and that Scrapy uses to scrape information from a website  They must subclass Spider and define the initial requests to be made, and optionally, how to follow links in pages and parse the downloaded page content to extract data

>> tutorial/spiders (quotes_spider.py)

from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

>> name : (identifies the spider, must unique within a project)
>> start_requests(): must return an iterable of Requests which the Spider will begin to crawl from.
>> parse() : method (handle response for each request) ,  method usually parses the response, extracting the scraped data as dicts and  also finding new URLs to follow and creating new requests (Request) from them.

## scrapy crawl quotes (to run application)

Scrapy schedules the scrapy.Request objects returned by the start_requests method of the Spider. Upon receiving a response for each one, it instantiates Response objects and calls the callback method associated with the request (in this case, the parse method) passing the response as an argument.

## A shortcut to the start_requests method¶ (start_urls=["",""]) parse called default

## Extracting data (using selectors)

> scrapy shell 'url' (to starts scrapping)
>> response.css("tagName") 
// [<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>> response.css("tagname::text").getall() or .get()

>> ::text , means only select text directly inside a tag, if omit will get element

>> NOTE: getall() list return , get() single

>> response.css("title::text")[0].get() (possible but error raises if idx out of bound)

>> css (named as SelectorList), returns None if not presented. eg: get()

>> scrapy crawl quotes -O quotes.json (saves it into json) [-O overwrites , -o appends]

note: appending to a JSON file makes the file contents invalid JSON

>>  scrapy crawl quotes -o quotes.jsonl (saves it into json lines) (append possible)

## Using spider arguments

>> scrapy crawl quotes -O quotes-humor.json -a tag=humor (These arguments are passed to the Spider’s __init__ method and become spider attributes by default.)

>> self.tag (can access)

def start_requests(self):
        url = "https://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url, self.parse)

Note : If you pass the tag=humor argument to this spider, you’ll notice that it will only visit URLs from the humor tag, such as https://quotes.toscrape.com/tag/humor