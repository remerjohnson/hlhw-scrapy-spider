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
            descriptions = r.xpath('//p').extract()
            h3s = response.xpath('//h3').extract()
            h3s = h3s[1:]
            for description, title in zip(descriptions, h3s):
                yield {'description': description.strip().replace('<p>', '').replace('</p>', ''),
                      'title': title.strip().replace('<h3>', '').replace('</h3>', '')
                      }
            