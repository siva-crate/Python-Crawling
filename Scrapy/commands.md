## All Cheatsheet

> response.css("tagName") # extarct data in a list, we should loop

> response.css("tagName::text") # extract content only

> response.css("tagName.className") #extact with specified className

> response.css("tagName.className").getall()

> response.css("tagName.className").get()

> scrapy crawl quotes -O quotes.json (save in json) [-O overwrites , -o append]

> scrapy crawl quotes -O quotes.jsonl (supports append for json)

## Following links (The first thing to do is extract the link to the page)

> response.css("li.next a::attr(href)").get()

> response.css("li.next a").attrib["href"] # next is a className

>   next_page = response.urljoin(url) #following link
    yield scrapy.Request(next_page, callback=self.parse)


## A shortcut for creating Requests ( response.follow supports relative URLs directly , no need to call urljoin. )

> Note that response.follow just returns a Request instance; you still have to yield this Request.

> yield response.follow(url, callback=self.parse)

for href in response.css("ul.pager a::attr(href)"):
    yield response.follow(href, callback=self.parse)

## For <a> elements there is a shortcut: response.follow uses their href attribute automatically. So the code can be shortened further:

> for a in response.css("ul.pager a"):
    yield response.follow(a, callback=self.parse)

## To create multiple requests from an iterable, you can use response.follow_all instead:

> yield from response.follow_all(response.css("ul.pager a"), callback=self.parse)

> yield from response.follow_all(css="ul.pager a", callback=self.parse)

> def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }
'''
Another interesting thing this spider demonstrates is that, even if there are many quotes from the same author, we don’t need to worry about visiting the same author page multiple times. By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of hitting servers too much because of a programming mistake

As yet another example spider that leverages the mechanism of following links, check out the CrawlSpider class for a generic spider that implements a small rules engine that you can use to write your crawlers on top of it.

'''

for href in response.xpath("//a/@href").getall():
            yield scrapy.Request(response.urljoin(href), self.parse)

## A valid use case is to set the http auth credentials used by HttpAuthMiddleware or the user agent used by UserAgentMiddleware:

> scrapy crawl myspider -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot

## CrawlSpider

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com"]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=(r"category\.php",), deny=(r"subsection\.php",))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r"item\.php",)), callback="parse_item"),
    )

    def parse_item(self, response):
        self.logger.info("Hi, this is an item page! %s", response.url)
        item = scrapy.Item()
        item["id"] = response.xpath('//td[@id="item_id"]/text()').re(r"ID: (\d+)")
        item["name"] = response.xpath('//td[@id="item_name"]/text()').get()
        item["description"] = response.xpath(
            '//td[@id="item_description"]/text()'
        ).get()
        item["link_text"] = response.meta["link_text"]
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.follow(
            url, self.parse_additional_page, cb_kwargs=dict(item=item)
        )

    def parse_additional_page(self, response, item):
        item["additional_data"] = response.xpath(
            '//p[@id="additional_data"]/text()'
        ).get()
        return item

## divs = response.xpath("//div")
> for p in divs.xpath(".//p"):  # this is wrong - gets all <p> from the whole document
        print(p.get())

Because an element can contain multiple CSS classes, the XPath way to select elements by class is the rather verbose:


sel = Selector(

    text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>'

)

> sel.css(".shout").xpath("./time/@datetime").getall()

## Beware of the difference between //node[1] and (//node)[1]

//node[1] selects all the nodes occurring first under their respective parents.

(//node)[1] selects all the nodes in the document, and then gets only the first of them.

xp = lambda x: sel.xpath(x).getall()
xp("//li[1]")

xp("(//li)[1]")

# `$val` used in the expression, a `val` argument needs to be passed

response.xpath("//div[@id=$val]/a/text()", val="images").get()

