from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymysql

#chrome无界面运行
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'python'
db = pymysql.connect(host='localhost', user='root', password='cxc123', port=3306, db='spider')

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            #等待节点加载完成    选择父节点为（选择ID为mainsrp-pager 内 div属性为form的节点）的所有input节点
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            #等待节点可点击
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
            #等待某个节点文本包含某文字
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            #取到某个PyQuery类型的节点后，就可以调用attr()方法来获取属性
            #find查找子节点
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mysql(product)


# data = {
#     'title':'20120001',
#     'image':'Bob',
#     'age':20
# }

def save_to_mysql(product):
    table = 'taobao'
    keys = ','.join(product.keys())
    values = ','.join(['%s'] * len(product))
    cursor = db.cursor()
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
    update = ','.join(["{key} = %s".format(key=key) for key in product])
    sql += update
    try:
        if cursor.execute(sql, tuple(product.values())*2):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()

MAX_PAGE = 10
def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    db.close()

if __name__ == '__main__':
    main()

