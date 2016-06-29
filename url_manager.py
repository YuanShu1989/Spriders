#! python2
# -*- coding: utf-8 -*-
# @Date    : 2016-06-27 10:49:08
# @Author  : Yuan Su (tomcatyuanshu@gmail.com)


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        '''
        adding new url to url manager
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        adding list of urls to url manager
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        determine a url is crawled.
        '''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''
        get a url which is not crawled from url manager
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
