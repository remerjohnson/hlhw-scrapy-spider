# -*- coding: utf-8 -*-
'''
HLHW Events Scrapy Spider 
How to run (and export to csv): 
$ scrapy crawl events -o data.csv
'''

import scrapy

class EventsSpider(scrapy.Spider):
    name = "events"

    def start_requests(self):
        url = 'https://libraries.ucsd.edu/visit/library-workshops/holocaust-living-history-workshop/events/2018-2019.html'
        for u in url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for r in response.xpath('//html'):
            description = r.xpath('//p').extract()
            for d in description:
                yield {'description': d.strip().replace('<p>', '').replace('</p>', '')}
            