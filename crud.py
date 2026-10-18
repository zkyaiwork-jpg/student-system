from database import get_connection     # 调用 database文件中的 get_connection 函数


def get_students():

    # 调用 get_connection()函数,创建一个 Connection 连接对象,由 conn 变量指向 Connection 对象
    conn = get_connection()

    # 调用 Connection 对象的 cursor()方法,创建一个游标对象,由 cursor 变量指向 Cursor 对象
    cursor = conn.cursor()

    # 编写SQL语句
    sql = "select * from students"

    # 使用 Cursor 对象的 execute 方法,向MySQL数据库发送SQL语句,让MySQL执行
    cursor.execute(sql)

    # 使用 Cursor 对象的 fetchall方法, 获取SQL查询返回的全部数据(fetchone返回一条数据)
    rows = cursor.fetchall()

    # 创建students列表
    students = []

    # 遍历rows
    for row in rows:
        # 创建字典student
        student = {
            "id":row[0],
            "name":row[1],
            "age":row[2],
            "email":row[3],
        }
        # 将字典添加到列表中
        students.append(student)

    # 关闭游标对象,释放系统资源
    cursor.close()

    # 关闭数据库连接
    conn.close()

    # 返回查询结果
    return students

def create_student(name,age,email):

    # 创建连接对象
    conn = get_connection()

    # 创建游标对象
    cursor = conn.cursor()

    # 编写SQL语句
    sql = """
    insert into students (name,age,email)
    values (%s,%s,%s)
    """

    # 向MySQL发送SQL语句和参数
    cursor.execute(sql,(name,age,email))

    # 提交事务,让修改真正保存到数据库
    conn.commit()

    # 获取刚刚插入数据的自增id
    student_id = cursor.lastrowid

    cursor.close()

    conn.close()

    return student_id

def get_student_by_id(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    select * from students
    where id = %s
    """

    cursor.execute(sql,(student_id,))

    row = cursor.fetchone()

    cursor.close()

    conn.close()

    if row:
        return {
            "id":row[0],
            "name":row[1],
            "age":row[2],
            "email":row[3]
        }

    return None

def del_student(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    delete from students
    where id = %s
    """

    # 逗号的作用: python中(3)不是元组,是数字. 而(3,)才是单元素元组, PyMySQL参数需要元组
    cursor.execute(sql,(student_id,))

    # 提交事务
    conn.commit()

    # 查看删除了几条数据
    affected_rows = cursor.rowcount

    cursor.close()

    conn.close()

    return affected_rows

def update_student(student_id,name,age,email):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    update students
    set name = %s,
        age = %s,
        email = %s
    where id =%s
    """

    cursor.execute(sql,(name,age,email,student_id))

    conn.commit()

    # 查看修改了几条数据
    affected_rows = cursor.rowcount

    cursor.close()

    conn.close()

    return affected_rows

if __name__ == "__main__":
    pass
