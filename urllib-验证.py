from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)



#这里首先实例化HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm对象，它利用add_password()添加进去用户名和密码，这样就建立了一个处理验证的Handler。
#接下来，利用这个Handler并使用build_opener()方法构建一个Opener，这个Opener在发送请求时就相当于已经验证成功了。
#接下来，利用Opener的open()方法打开链接，就可以完成验证了。这里获取到的结果就是验证后的页面源码内容。
