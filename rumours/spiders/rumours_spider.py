import scrapy
from scrapy import Request
from rumours.items import RumoursItem, RumoursPost

class RumoursSpider(scrapy.Spider):
    name = "rumours"
    allowed_domains = ["www.pprune.org"]
    start_urls = ["http://www.pprune.org/rumours-news-13/"]
    def parse(self, response):
        count = 0
        for sel in response.xpath("//table[@id='threadslist']/tbody[2]/tr"):
            title = sel.xpath("td[3]/div/a[starts-with(@id, 'thread_title')]/text()").extract()
            url = sel.xpath("td[3]/div/a[starts-with(@id, 'thread_title')]/@href").extract()
            num_replies = sel.xpath("td[5]/a/text()").extract()
            views = sel.xpath("td[6]/text()").extract()
            author = sel.xpath("td[3]/div[2]/span/text()").extract()
            item = RumoursItem()
            item['title'] = title[0]
            item['url'] = url[0]
            item['num_replies'] = num_replies[0]
            item['author'] = author[0]
            item['views'] = views[0]
            item['replies'] = []
            yield Request(url[0], callback=self.parseThread, meta={"item": item})

    def parseThread(self, response):
        pitem = response.meta["item"]
        for sel in  response.xpath("//div[@id='posts']/div/table"):
            div = []
            username = sel.xpath("tr[2]/td/div/a/text()").extract()
            div.append(sel.xpath("tr[2]/td/div[2]/div[1]/text()").extract())
            div.append(sel.xpath("tr[2]/td/div[2]/div[2]/text()").extract())
            div.append(sel.xpath("tr[2]/td/div[2]/div[3]/text()").extract())
            div.append(sel.xpath("tr[2]/td/div[2]/div[4]/text()").extract())
            datetime = sel.xpath("tr[1]/td[1]/text()").extract()
            content = sel.xpath("tr[2]/td[2]/div[starts-with(@id, 'post_message')]/text()").extract()
            item = RumoursPost()
            
            for x in div:
                field = None
                if len(x) > 0:
                    if "Posts" in x[0]:
                        field = "posts"
                    if "Age" in x[0]:
                        field = "age"
                    if "Join Date" in x[0]:
                        field = "join_date"
                    if "Location" in x[0]:
                        field = "location"
                    if field is not None:
                        item[field] = x[0].strip().split(":")[1].strip()
            
            item['datetime'] = datetime[2].strip()
            item['content'] = ''
            for x in content:
                item['content'] += x
            item['content'] = item['content'].strip()
            item['username'] = username[0].strip()
            pitem['replies'].append(item);
        nextpage = response.xpath("//a[text()='>']/@href").extract()
        if len(nextpage) > 0:
            yield Request(nextpage[0], callback=self.parseThread, meta={"item": pitem})
        yield pitem