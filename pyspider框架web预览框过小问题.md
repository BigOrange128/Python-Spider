# 解决pyspider框架web预览框过小问题
>谷歌浏览器使用pyspider框架时，web预览框只有一小行。

#### 在网上查到解决办法：
1.从该合并请求中将debug.min.css的改动后的内容复制下来。[请求地址](https://github.com/ok2fly/pyspider/blob/abcfc98970be27dd97901479675ce6df39be63fc/pyspider/webui/static/debug.min.css)

2.在web ui的安装机器上找到debug.min.css文件，替换掉里面的内容。参考文件路径:vi /usr/local/lib/python2.7/site-packages/pyspider/webui/static/debug.min.css
    
#### 经过他的方法后有时还是不能够正常显示，需要在web显示界面下再次点击run按钮，即可显示正常大小。    
参考的地址
<http://www.cnblogs.com/zhaohz/p/9300558.html>
