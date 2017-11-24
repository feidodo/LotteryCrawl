import scrapy

from tutorial.items import LotteryItem

class LotterySpider(scrapy.Spider):
    name = "lottery"
    #allowed_domains = ["lottery.gov.cn"]
    start_urls = [
    "http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt"
    #"http://www.lottery.gov.cn/historykj/history.jspx?_ltype=pls",
    #"http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw",
    #"http://www.lottery.gov.cn/historykj/history.jspx?_ltype=qxc"
    ]

    def parse(self, response):
        for lottery in response.xpath('//div[@class="result"]/table/tbody/tr'):
            item = LotteryItem()
            info = lottery.xpath('./td/text()').extract()
            #print len(info)
            item['Id'] = info[0]
            item['num_prefix'] = "{0} {1} {2} {3} {4}".format(info[1],info[2],info[3],info[4],info[5])
            item['num_postfix'] = "{0} {1}".format(info[6],info[7])
            item['sales'] = info[16]
            item['pool'] = info[17]
            item['date'] = info[18]
            item['detail_link'] = lottery.xpath('./td/a/@href').extract_first()
            yield item
        links = response.xpath('//div[@class="page"]/div/a')
        next_page_url = links[2].xpath('@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
