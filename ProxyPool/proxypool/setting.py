# Mysql数据库地址，用户名，数据库名
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_DB = 'spider'

# Mysql端口
MYSQL_PORT = 3306

# Mysql密码
MYSQL_PASSWORD = '***'

#Mysql表名
MYSQL_TB = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10