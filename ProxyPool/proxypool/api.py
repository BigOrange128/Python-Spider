from flask import Flask, g
from .db import MysqlClient

__all__ = ['app']

app = Flask(__name__)

def get_conn():
    if not hasattr(g, 'pymysql'):
        g.mysql = MysqlClient()
    return g.mysql

@app.route('/')
def index():
    return '<h2>Welcom to Proxy Pool System</h2>'

@app.route('/random')
def get_proxy():
    """
    获得一个随机代理
    :return: 随机代理
    """
    conn = get_conn()
    return  conn.random()

@app.route('/count')
def get_counts():
    """
    获取代理池内的代理总数量
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run()