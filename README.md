# AutoSavePages
自动保存浏览打开的页面到数据库当中



当前已实现功能：

- [ ] 浏览器（Google）打开新页面自动抓取url并发送给后台
- [ ] 后台对接收的URL进行保存



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
pip install flask flask_mysqldb flask_cors tldextract
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
CREATE TABLE visited_urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(2048) NOT NULL,
    title VARCHAR(255) NOT NULL,
) CHARSET=utf8mb4;
```

