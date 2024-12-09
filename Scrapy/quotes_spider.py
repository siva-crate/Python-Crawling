import scrapy

## pip install Twisted==22.10.0 (if EPollReactor error) occurs of scrapy is reinstalled.
## -o quotes.jsonl (creating a json file) # json lines format (jsonl)

## scrapy runspider quotes_spider.py

class QuotesSpider(scrapy.Spider):
      name = "quotes"
      start_urls = [
            "https://quotes.toscrape.com/tag/humor/",
      ]

      def parse(self, response):
            for quote in response.css("div.quote"): #tag.className
                  print(quote.xpath("span/small/text()"), "####")
                  # [<Selector query='span/small/text()' data='Jane Austen'>]
                  yield {
                  "author": quote.xpath("span/small/text()").get(), #span>small>text
                  "text": quote.css("span.text::text").get(), #tag.className::text returns content
            }


            #paginations
            next_page = response.css('li.next a::attr("href")').get()
            if next_page is not None:
                  yield response.follow(next_page, self.parse)

'''
      work flow:

      When you ran the command scrapy runspider quotes_spider.py, 
      
      Scrapy looked for a Spider definition inside it and ran it through its crawler engine.

      The crawl started by making requests to the URLs defined in the "start_urls attribute" (in this case, only the URL for quotes in the humor category) and called the "default callback method parse", passing the response object as an argument. In the parse callback, we loop through the quote elements using a CSS Selector, "yield a Python dict with the extracted quote text and author", 
      
      "look for a link to the next page and schedule another request using the same parse method as callback."

'''