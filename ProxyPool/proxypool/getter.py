from ProxyPool.proxypool.tester import Tester
from ProxyPool.proxypool.db import MysqlClient
from ProxyPool.proxypool.crawler import Crawler
from ProxyPool.proxypool.setting import *
import sys

class Getter():
    def __init__(self):
        self.mysql = MysqlClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.mysql.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.mysql.add(proxy)