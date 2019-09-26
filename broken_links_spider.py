from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import config


class BrokenItem(Item):
    url = Field()
    referer = Field()
    status = Field()


class BrokenLinksSpider(CrawlSpider):
    name = 'BrokenLinksSpider'
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def __init__(self, name=None, urls=None, domains=None, httpstatus=None, **kwargs):
        self.name = name or config.name
        self.allowed_domains = domains.split(',') if domains else config.allowed_domains
        self.allowed_domains = [d.split('://')[-1].rstrip('/') for d in self.allowed_domains]
        self.start_urls = urls.split(',') if urls else config.start_urls
        self.handle_httpstatus_list = map(int, httpstatus.split(',')) if httpstatus else config.httpstatus_list
        super(BrokenLinksSpider, self).__init__(**kwargs)

    def parse_item(self, response):
        if response.status in self.handle_httpstatus_list:
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            return item
