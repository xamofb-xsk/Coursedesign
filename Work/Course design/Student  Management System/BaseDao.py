import sqlite3
import Student as student

s = student.Student()
dbstr = "mydb.db"


# 1.查询所有学生信息
def getAll():
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    cur.execute("select * from student")
    data = cur.fetchall()
    cur.close()
    connect.close()
    return data


# 根据学生姓名查询学生信息
def getStudentBySname(s):
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    cur.execute("select * from student where name='%s'" % (s.getSname()))
    data = cur.fetchall()
    connect.close()
    cur.close()
    return data


# 根据sid查询单个学生信息
def getStudentBySid(s):
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    cur.execute("select * from student where sid='%s'" % (s.getSid()))
    data = cur.fetchall()
    connect.close()
    cur.close()
    return data


# 添加学生信息
def addStudent(s):
    # list1 = []
    # list1.append(s.getSid()())
    # list1.append(s.getSname())
    # list1.append(s.getSphone)
    # list1.append(s.getSaddress)
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    cur.execute("insert into student values('%s','%s','%s','%s')" % (s.getSid(), s.getSname(), s.getSphone(), s.getSaddress()))
    connect.commit()
    cur.close()
    connect.close()

# 删除学生信息
def delStudent(s):
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    cur.execute("delete from student where sid='%s'" % s.getSid())
    connect.commit()
    cur.close()
    connect.close()

# 修改学生信息
def updStudent(s):
    connect = sqlite3.connect(dbstr)
    cur = connect.cursor()
    sql = "update student set name='%s',phone='%s' ,address='%s' where sid='%s'" % (
         s.getSname(), s.getSphone(), s.getSaddress(), s.getSid())
    cur.execute(sql)
    connect.commit()
    connect.close()


# 根据查询条件查询学生信息
def selectStu(s):
    connect = sqlite3.connect(dbstr)
    cursor = connect.cursor()
    sql = "select * from student where 1=1"
    if s.getSid() != "":
        sql = sql + " and sid='%s'" % (s.getSid())
    if s.getSname() != "":
        sql = sql + " and name like '%%%s%%'" % (s.getSname())
    if s.getSphone() != "":
        sql = sql + " and phone='%s'" % (s.getSphone())
    if s.getSaddress() != "":
        sql = sql + " and address='%s'" % (s.getSaddress())
    cursor.execute(sql)
    data = cursor.fetchall()
    connect.close()
    return data

