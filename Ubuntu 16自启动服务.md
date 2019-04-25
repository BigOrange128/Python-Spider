## Ubuntu16自动启动服务
> 将某项服务配置为自动启动服务。在Ubuntu 14的系统，可以用upstart的方式。但在16以后的版本中这个命令失效了。

以创建Gunicorn服务为例
### 创建service文件
> /lib/systemd/system/目录下，创建服务脚本 blog.service

    [Unit]
    After=syslog.target network.target remote-fs.target nss-lookup.target
    [Service]
    # 你的用户
    User=root
    # 你的目录
    WorkingDirectory=/root/sites/demo.blog.com/tanblog
    # gunicorn启动命令
    ExecStart=/root/sites/demo.blog.com/env/bin/gunicorn --bind unix:/tmp/10.8.0.76 tanblog.wsgi:application
    Restart=on-failure
    [Install]
    WantedBy=multi-user.targ

### 启动服务

    #手动启动
    systemctl start blog.service
    #添加到开机自动运行
    systemctl enable siar.service
