import scrapy

class mySpidy(scrapy.Spider):
    name="practice"
    start_urls=["https://docs.scrapy.org/en/latest/intro/tutorial.html"]

    #div::div (invalid) , .data
    def parse(self,response):

        # div_container=response.css("div") # it returns all in list
        # for i in div_container: # html data
        #     with open('../divContent.txt',"a") as file:
        #         print("file is opened")
        #         file.write(str(i)+"\n new line \n")
        #     print()
        # print(response.css("div"))

        print()
        for i in response.css("div.wy-grid-for-nav a::text"): # extracting all matched
            print(str(i.get()).strip())
            break
        print(response.css("div.wy-grid-for-nav a::text").getall())
        print()
        print(response.css("h1").get())
        print(response.css("h1::text").get())
        
        print(response) #<200 https://docs.scrapy.org/en/latest/intro/tutorial.html>
        print(response.status) # returns 200
        print(response.url) # return url

        print(response.css("h1::text").re(r"Scrapy.*"))

        print(response.css("div.wy-grid-for-nav a::text").re(r"S.*"))

        print(response.css("div.wy-grid-for-nav a::text").re(r"S\w+y"))

        print(response.css("div.wy-grid-for-nav a::text").re(r"(\w+) (\w+)"))

        print(response.xpath("//h1"))
        # [<Selector query='//h1' data='<h1>Scrapy Tutorial<a class="headerli...'>]
        print(response.xpath("//h1").get())
        # <h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this heading">¶</a></h1>
        print(response.xpath("//h1//a").get())
        # <a class="headerlink" href="#scrapy-tutorial" title="Permalink to this heading">¶</a>
        print(response.xpath("//h1//a/href").get()) # None

        print(response.css("h1 a::attr(href)").get())

        print(response.css("h1 a").attrib["href"])

        '''
            Now let’s see our spider, modified to recursively follow the link to the next page, extracting data from it:
        '''

        next_page=response.css("h1 a").attrib["href"]
        if next_page is not None:
            next_page=response.urljoin(next_page)
            print(next_page)
            #yield scrapy.Request(next_page,callback=self.parse)

        