from urllib import request, error

try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

# 这样就可以做到先捕获HTTPError，获取它的错误状态码、原因、headers等信息。
# 如果不是HTTPError异常，就会捕获URLError异常，输出错误原因。
# 最后，用else来处理正常的逻辑。这是一个较好的异常处理写法。


# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')
# 可以发现，reason属性的结果是socket.timeout类。
# 所以，这里我们可以用isinstance()方法来判断它的类型，作出更详细的异常判断。