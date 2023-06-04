from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# MySQL 配置
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mysql'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/save_url', methods=['POST'])
def save_url():
    url = request.form.get('url')

    # 储存 URL 到数据库
    store_url_to_database(url)

    return 'Success', 200

@app.route('/get_url', methods=['GET'])
def get_url():
    return 'Success'


def store_url_to_database(url):
    # 在这里添加保存 URL 至您数据库的代码，例如 MySQL、Postgres SQL、MongoDB 等，根据您的实际需求来实现。
    # 连接到 MySQL 数据库
    cursor = mysql.connection.cursor()

    # 在这里编写 SQL 语句，将 URL 插入到您的数据表中
    # 假设您的数据库中有一个名为 "visited_urls" 的表，其中包含两个字段：id 和 url
    sql_query = f"INSERT INTO visited_urls (url) VALUES ('{url}')"

    # 执行 SQL 语句
    cursor.execute(sql_query)

    # 提交更改
    mysql.connection.commit()

    # 关闭
    cursor.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
