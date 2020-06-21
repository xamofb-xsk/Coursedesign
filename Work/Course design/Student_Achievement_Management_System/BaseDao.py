import sqlite3
import Student as student

s = student.Student()
dbstr = "mydb.db"  # 设置全局变量：数据库名称


# 得分点1，使用数据库sqlite3
# 获取数据库有几行
def get_data():
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    cur.execute("select count(*) from student")  # 使用游标执行SQL语句，这里是查询数据库行数
    data = cur.fetchall()  # 获取结果集中的所有
    data = " ".join('%s' % id for id in data)  # 将元组转换为字符串
    data = int(data)
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    return data


# 查询所有学生信息
def getAll():
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    data = get_data()  # 获取行数
    for i in range(0, data + 1):  # 通过for循环逐行读取出数据库数据
        cur.execute("select * from student where count=%d" % i)
        dat = cur.fetchall()  # 获取结果集中的所有
        if not dat:
            continue
        print(dat)
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


# 根据sid查询单个学生信息
def getStudentBySid(s):
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    cur.execute("select * from student where sid='%s'" % (s.getSid()))  # 通过学号查询学生信息
    data = cur.fetchall()  # 获取结果集中的所有
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    print(data)


# 添加学生信息
def addStudent(s):
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    data = get_data()  # 获取行数
    cur.execute("insert into student values('%s','%s','%s','%s','%s','%s','%s','%d')" % (
        s.getSid(), s.getSname(), s.getSphone(), s.getSenglish(), s.getSmath(), s.getSphysical(), s.getScomputer(),
        data))  # 执行insert语句将输入的的数据写入数据库
    connect.commit()  # 提交数据
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


# 删除学生信息
def delStudent(s):
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    cur.execute("delete from student where sid='%s'" % s.getSid())  # 删除指定学号的数据
    connect.commit()  # 提交数据
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


# 修改学生信息
def updStudent(s):
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    sql = "update student set name='%s',phone='%s' ,english='%s',math='%s',physical='%s',computer='%s' where sid='%s'" % (
        s.getSname(), s.getSphone(), s.getSenglish(), s.getSmath(), s.getSphysical(), s.getScomputer(), s.getSid())
    cur.execute(sql)  # 通过学号修改数据
    connect.commit()  # 提交数据
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接


# 查询学生信息，辅助修改信息使用
def selectStu(s):
    connect = sqlite3.connect(dbstr)  # 连接数据库
    cur = connect.cursor()  # 通过连接获取游标，返回Cursor对象，用于执行sql语句并获得结果
    cur.execute("select * from student where 1=1")
    data = cur.fetchall()  # 获取结果集中的所有
    cur.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
    return data
