# 通过关键词爬取淘宝商品的信息
>原来用selenium做过一次，最近淘宝有了改动，需要登录才可以使用搜索功能。最近又用requests写了一个，加入了cookie。

#### 项目分析
一般不使用框架自己写的爬虫，也就可以分为3个模块。获取页面，解析页面，保存数据。这次的项目即是如此。
#### 获取页面模块
下面先看代码
    
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
    
首先定义请求头，模拟浏览器访问，还有加入cookie来模拟登陆。使用requests向目标链接发送get请求，
如果返回状态码为200则将网页源代码返回。
#### 解析页面模块
下面先看代码

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

我们使用正则表达式来获取想要的数据，正则表达式的使用不多叙述。首先定义了正则表达式，一组数据获得4个关键字数据。
然后对全文查找，这样查找出来的结果就像是一个嵌套列表。然后我们依次从中取出每组数据，然后再分别取出每组数据中的每一项
来构造字典，将字典返回。
#### 存储模块
下面先看代码

    def save_csv(item):
    with open('taobao.csv', 'a+') as csvfile:
        fieldnames = ['title', 'price', 'loc', 'nick']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow(item)
        
存储的方式有很多，可以对接数据库。这次为了简便就保存为csv文件了。（一般参数中会指定编码格式为utf-8，但是我这里制定后，Excel打开会乱码，就没指定。）
#### 关于构造请求链接
淘宝搜索物品的请求链接看起来很长很繁琐，其实不然，只需要其中的两个参数就可以正常访问了。

我们可以搜索一个物品，然后翻几页，观察url变换，你就会发现变化的有两个主要参数search?q=后面跟关键词，&s=后面跟一个数字，每次变化44。
这样我们就可以构造一个这样的类似这样的请求来进行访问。

     https://s.taobao.com/search?q=vans&s=44
     url = 'https://s.taobao.com/search?q=' + KYE_WORD + "&s={}".format(MAX_PAGE)
     
#### main函数调度
写好模块以后我们就可以定义main函数来进行调用，实现整个程序的运行。

#### 完整代码地址
<https://github.com/BigOrange128/Python-Spider/blob/master/%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81-GET.py>
