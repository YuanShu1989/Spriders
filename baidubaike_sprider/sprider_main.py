#! python2
# -*- coding: utf-8 -*-
# @Date    : 2016-06-27 10:48:31
# @Author  : Yuan Su (tomcatyuanshu@gmail.com)
'''
循环抓取百度百科上的url
'''


import url_manager
import html_downloader
import html_parser
import html_outputer


class SpriderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        # 记录爬取第几个url
        count = 1
        self.urls.add_new_url(root_url)
        # url管理器有新的url的时候
        while self.urls.has_new_url():
            try:
                # 获取一个待爬取url
                new_url = self.urls.get_new_url()
                print('crawl %d : %s' % (count, new_url))
                # 下载这个页面
                html_cont = self.downloader.download(new_url)
                # 解析页面获得新的url列表和数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 把新的url列表添加到url管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count += 1

            except:
                print('crawl failed! ')

        # 输入数据
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_sprider = SpriderMain()
    obj_sprider.crawl(root_url)
