import requests
from requests.exceptions import RequestException
import re
from time import sleep
import csv

MAX_PAGE = 3
KYE_WORD = 'python'

def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'cookie':''
        }
        response = requests.get(url, headers = headers)
        if response.status_code == 200 :
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    content = '"raw_title":"(.*?)".*?"view_price":"(.*?)".*?"item_loc":"(.*?)".*?"nick":"(.*?)"'
    pattern = re.compile(content, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title':item[0],
            'price':item[1],
            'loc':item[2],
            'nick':item[3]
        }

def save_csv(item):
    with open('taobao.csv', 'a+', encoding = 'utf-8') as csvfile:
        fieldnames = ['title', 'price', 'loc', 'nick']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow(item)


def main():
    #https://s.taobao.com/earch?q=vans&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
    for i in range(MAX_PAGE):
        S_AGE = i * 44
        url = 'https://s.taobao.com/search?q=' + KYE_WORD + "&s={}".format(MAX_PAGE)
        html = get_page(url)
        sleep(2)
        for item in parse_page(html):
            print(item)
            save_csv(item)

if __name__ == '__main__':
    main()
