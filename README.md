# AutoSavePages
自动保存浏览打开的页面到数据库当中



当前已实现功能：

- [ ] 浏览器（Google）打开新页面自动抓取url并发送给后台
- [ ] 后台对接收的URL进行保存
  - [ ] 使用远程服务器接受URL




预计添加功能

- [ ] ~~针对保存的URL进行过滤筛选，转换成EPUB文件~~

  > EPUB貌似保存下来的内容不太友好。。。
  >
  > PDF在使用wkhtmltopdf的时候被卡住了，进度一直在50%。。。
  >
  > MHTML 需要权限。。。
  >
  > 直接保存URL，再加一个标题一起保存到DB当中吧

- [ ] ~~对转换的EPUB进行归档整理~~

- [ ] ~~一个简单的管理页面对转换的EPUB文件展示~~

- [ ] 对保存的URL进行网站分类



### 浏览器插件

- 修改后台服务器地址。默认是本地：

  ```js
  const endpoint = "http:localhost:5000/save_url";
  ```

  images文件下放的是icon，可以替换

- 使用Google浏览器，打开开发者模式，导入`auto-save-visited-pages` 文件夹



### 后台

进入 `AutoSavePage` 文件夹

下载依赖:

```
pip install flask flask_mysqldb flask_cors 
```

修改数据库配置：

```js
# MySQL 配置
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mysql'
```

修改监听端口：

```js
 app.run(host='0.0.0.0', port=5000)
```

数据库建表（简单版）：

```sql
create table visited_urls
(
    id               int auto_increment
        primary key,
    url              varchar(2048)                       not null,
    visit_time       timestamp default CURRENT_TIMESTAMP null,
    title            varchar(2048)                       null,
    top_level_domain varchar(255)                        not null
)
    collate = utf8mb4_unicode_ci;
```



### 服务器配置

首先需要python 环境（最好python 3） ，同时安装pip

然后install相关的module

```
pip install flask mysql-connector-python Flask-MySQL flask_mysqldb flask_cors bs4 requests tldextract
```

在安装flask_mysqldb的过程中遇到坑，要去下载python连接MySQL的驱动才行。。。

然后在服务器上（CentOS）的一下目录创建一个新的service,例如： auto_save.service

```
/etc/systemd/syetem/
```

编辑auto_save.service里面的内容：

```
[Unit]
Description=Auto Save URL script
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /root/tools/auto_save_page/app.py

[Install]
WantedBy=multi-user.target
```

/usr/bin/python3 表示python3 的位置，使用which python3 命令可以看到

/root/tools/auto_save_page/app.py  脚本位置



然后：

```
systemctl daemon-reload
systemctl enable auto_save.service
systemctl start auto_save.service
# 查看状态
systemctl status auto_save.service
```



另外打开防火墙：

```
firewall-cmd --permanent --zone=public --add-port=5000/tcp
firewall-cmd --reload
firewall-cmd --list-all
```

