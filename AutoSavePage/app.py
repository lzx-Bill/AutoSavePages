from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from urllib.parse import urlsplit

app = Flask(__name__)

CORS(app)

# MySQL 配置
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mysql'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

mysql = MySQL(app)


@app.route('/save_url', methods=['POST'])
def save_url():
    url = request.form.get('url')

    if not url or not is_valid_url(url):
        return 'Bad request: invalid or missing url parameter', 400

    title = get_title(url)

    # 储存 URL 到数据库
    store_url_to_database(url, title)

    return 'Success', 200

@app.route('/get_url', methods=['GET'])
def get_url():
    return 'Success'


def is_valid_url(url):
    try:
        result = urlsplit(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def get_title(url):
    response = requests.get(url)

    # 确保使用正确的字符编码
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    if soup.title:
        title = soup.title.string
    else:
        title = "No Title Found"

    return title

def store_url_to_database(url, title):
    # 在这里添加保存 URL 至您数据库的代码，例如 MySQL、Postgres SQL、MongoDB 等，根据您的实际需求来实现。
    # 连接到 MySQL 数据库
    cursor = mysql.connection.cursor()

    # 在这里编写 SQL 语句，将 URL 插入到您的数据表中
    # 假设您的数据库中有一个名为 "visited_urls" 的表，其中包含两个字段：id 和 url
    sql_query = f"INSERT INTO visited_urls (url,title) VALUES ('{url}','{title}')"

    # 执行 SQL 语句
    cursor.execute(sql_query)

    # 提交更改
    mysql.connection.commit()

    # 关闭
    cursor.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
