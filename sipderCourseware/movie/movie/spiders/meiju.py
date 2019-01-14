# -*- coding: utf-8 -*-
import scrapy


class MeijuSpider(scrapy.Spider):
    name = 'meiju'  # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫优先级、并发等设置。scrapy crawl [spider_name]
    allowed_domains = ['meijutt.com']   # 为了防止爬虫项目自动爬取到其它网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，检查allowed_domain书写是否正确。值是一级域名。
    start_urls = ['https://www.meijutt.com/new100.html']  # 第一个请求的url，所有请求的入口。

    def parse(self, response):
        pass
