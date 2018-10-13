# 谷歌浏览器使用pyspider框架时，web预览框只有一小行。

## 在网上查到解决办法：
  1. 从该合并请求中将debug.min.css的改动后的内容复制下来（只有一行代码）
    url: https://github.com/ok2fly/pyspider/blob/abcfc98970be27dd97901479675ce6df39be63fc/pyspider/webui/static/debug.min.css
  2. 在web ui的安装机器上找到debug.min.css文件，替换掉里面的内容
    vi /usr/local/lib/python2.7/site-packages/pyspider/webui/static/debug.min.css
    
## 经过他的方法后还是不能够正常显示，需要在web显示界面下再次点击run按钮。    
    源地址http://www.cnblogs.com/zhaohz/p/9300558.html
