from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'http://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# 这里我们在本地搭建了一个代理，它运行在9743端口上。
# 这里使用了ProxyHandler，其参数是一个字典，键名是协议类型（比如HTTP或者HTTPS等），键值是代理链接，可以添加多个代理。
# 然后，利用这个Handler及build_opener()方法构造一个Opener，之后发送请求即可。
