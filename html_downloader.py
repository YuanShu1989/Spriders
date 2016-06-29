#! python2
# -*- coding: utf-8 -*-
# @Date    : 2016-06-27 10:49:51
# @Author  : Yuan Su (tomcatyuanshu@gmail.com)
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
