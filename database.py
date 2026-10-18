import pymysql      # 作用:将python代码转换成MYSQL能理解的请求


# 创建连接函数
def get_connection():
    # 创建数据库连接
    conn = pymysql.connect(
        host = "localhost",     # mySQL 服务器地址
        port = 3306,            # mySQL 服务监听端口
        user = "root",          # 用户名
        password = "123456",    # 密码
        database = "student_db",# 进入哪一个数据库
        charset = "utf8"        # 使用什么字符编码
    )
    # 返回连接对象
    return conn

# 测试部分
try:
    conn = get_connection()

    print("数据库连接成功")

    conn.close()    # 关闭数据库连接
# 如果失败,捕获失败
except Exception as e:
    print("数据库连接失败")
    print(e)

