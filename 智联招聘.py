from pyspider.libs.base_handler import *

MAX_PAGE = 4
KEY_WORD = '爬虫'


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://sou.zhaopin.com/?jl=702&kw={0}&kt=3'.format(KEY_WORD), callback=self.index_page,
                   validate_cert=False, fetch_type='js')

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.contentpile__content__wrapper__item__info__box__jobname > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, fetch_type='js')
        for page in range(2, MAX_PAGE):
            self.crawl('https://sou.zhaopin.com/?p={0}&jl=702&kw={1}&kt=3'.format(page, KEY_WORD),
                       callback=self.index_page, validate_cert=False, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "money": response.doc('li > .info-money > strong').text(),
            "KeyWord": response.doc('.info-three').text(),
            "BrightSpot": response.doc('.pos-info-tit > div').text(),
            "require": response.doc('.pos-ul > p').text()
        }