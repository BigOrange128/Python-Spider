import pymysql
from ProxyPool.proxypool.error import PoolEmptyError
from ProxyPool.proxypool.setting import MYSQL_HOST, MYSQL_PORT, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DB, MYSQL_TB
from ProxyPool.proxypool.setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re

from random import choice

class MysqlClient(object):
    def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB):
        """
        初始化
        :param host:地址
        :param port: 短裤
        :param user: 用户
        :param password: 密码
        :param database: 数据库
        """
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.db.cursor()

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        select_sql = "SELECT * FROM {table} WHERE proxies_address='{proxy}'".format(table=MYSQL_TB, proxy=proxy)
        insert_sql = 'INSERT INTO {table}(proxies_address, score) VALUES(%s, %s)'.format(table=MYSQL_TB)
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('代理不符合规范', proxy, '丢弃')
            return
        if not self.cursor.execute(select_sql):
            try:
                if self.cursor.execute(insert_sql, (proxy, score)):
                    self.db.commit()
                    return True
            except:
                return False
    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获得，否则异常
        :return: 随机代理
        """
        select_sql = "SELECT proxies_address FROM {table} WHERE score='{maxscore}'".format(table=MYSQL_TB, maxscore=MAX_SCORE)
        selectall_sql = "SELECT proxies_address FROM {table} ORDER BY score DESC".format(table=MYSQL_TB)
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        if len(result):
            return choice(result)
        else:
            self.cursor.execute(selectall_sql)
            result = self.cursor.fetchall()
            if len(result):
                result = result[0:100]
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减一分，分数小于最小值，则代理删除
        :param proxy:代理
        :return:修改后的代理分数
        """
        select_sql = "SELECT score FROM {table} WHERE proxies_address='{proxy}'".format(table=MYSQL_TB, proxy=proxy)
        self.cursor.execute(select_sql)
        score = self.cursor.fetchone()[0]
        if score and score > MIN_SCORE:
            update_sql = 'UPDATE {table} SET score=%s WHERE proxies_address=%s'.format(table=MYSQL_TB)
            print('代理', proxy, '当前分数', score, '减1')
            try:
                self.cursor.execute(update_sql, (score-1, proxy))
                self.db.commit()
                return True
            except:
                return False
        else:
            delete_sql = "DELETE FROM  {table} WHERE proxies_address='{proxy}'".format(table=MYSQL_TB, proxy=proxy)
            print(delete_sql)
            print('代理', proxy, '当前分数', '移除')
            try:
                self.cursor.execute(delete_sql)
                self.db.commit()
                return True
            except:
                return False
    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        select_sql = "SELECT * FROM {table} WHERE proxies_address='{proxy}'".format(table=MYSQL_TB, proxy=proxy)
        return not self.cursor.execute(select_sql) == False
    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        update_sql = 'UPDATE {table} SET score=%s WHERE proxies_address=%s'.format(table=MYSQL_TB)
        try:
            self.cursor.execute(update_sql, (MAX_SCORE, proxy))
            self.db.commit()
            return True
        except:
            return False
    def count(self):
        """
        获取数量
        :return:数量
        """
        selectall_sql = "SELECT COUNT(proxies_address) FROM {table}".format(table=MYSQL_TB)
        self.cursor.execute(selectall_sql)
        return self.cursor.fetchone()[0]
    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        selectall_sql = "SELECT proxies_address FROM {table}".format(table=MYSQL_TB)
        self.cursor.execute(selectall_sql)
        return self.cursor.fetchall()

    def batch(self, start, stop):
        """
        批量获取
        :param start:开始位置
        :param stop: 结束位置
        :return: 代理列表
        """
        selectall_sql = "SELECT proxies_address FROM {table} ORDER BY score DESC".format(table=MYSQL_TB)
        self.cursor.execute(selectall_sql)
        result = self.cursor.fetchall()
        result = result[start:stop]
        return result
# def main():
#     s = MysqlClient()
    # s.random()
    # s.decrease(proxy = '192.168.1.0')
    # s.add(proxy = '192.168.1.2')
    # re = s.exists(proxy='192.168.1.1')
    # print(re)
    # s.max(proxy = '192.168.1.1')
    #s.count()
    #s.all()
if __name__ == '__main__':
    conn = MysqlClient()
    result = conn.batch(680,688)
    print(result)