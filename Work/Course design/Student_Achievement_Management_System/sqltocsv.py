import pandas
import sqlite3
import codecs
import csv


class Mysql_csv():
    def __init__(self):
        dbstr = "mydb.db"  # 设置数据库名称
        self.connect = sqlite3.connect(dbstr)  # 连接数据库
        self.cursor = self.connect.cursor()  # 设置游标

    def read(self):
        self.cursor.execute("select * from student where 1 = 1")  # 设置查询条件
        field_2 = self.cursor.fetchall()  # 输出所有的集
        return field_2

    def red_mysql_to_csv(self):
        with codecs.open(filename="data.csv", mode='w', encoding='utf-8')as f:  # 打开data.csv文件，模式设置为写入，编码设置为utf-8
            write = csv.writer(f, dialect='excel')  # 指定写入的文件和格式
            write.writerow(['学号', '姓名', '电话', '英语', '数学', '物理', '计算机二级', '行数'])
            results = self.read()
            for res in results:
                write.writerow(res) # 将数据库的文件写入到csv文件

    def __del__(self):
        self.cursor.close()
        self.connect.close()


def main():
    write = Mysql_csv()
    write.red_mysql_to_csv()


if __name__ == '__main__':
    main()
