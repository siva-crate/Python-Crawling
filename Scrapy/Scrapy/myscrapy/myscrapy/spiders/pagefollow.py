import scrapy

class mySpidy(scrapy.Spider):
    name="pageflw"

    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            #builds a full absolute URL using the urljoin() method

            '''
                yields a new request to the next page, registering itself as callback to handle the data extraction for the next page and to keep the crawling going through all the pages.

                Using this, you can build complex crawlers that follow links according to rules you define, and extract different kinds of data depending on the page it’s visiting.
            '''

            #yield scrapy.follow(url,callback=self.parse) (shortcut)

            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            