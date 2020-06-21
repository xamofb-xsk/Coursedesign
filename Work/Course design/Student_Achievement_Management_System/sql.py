import Student_Achievement_Management_System.BaseDao as sq
import Student_Achievement_Management_System.student_info_creat as sic
import Student_Achievement_Management_System.Student as s
import Student_Achievement_Management_System.sqltocsv as tocsv

stu = s.Student()
# 随机生成数据并导入到数据库文件中
for i in range(0, 1000):
    a = sic.Info()
    stu.setSid(a.xuehao())
    stu.setSname(a.name())
    stu.setSphone(a.phone())
    stu.setSenglish(a.english())
    stu.setSmath(a.math())
    stu.setSphysical(a.physical())
    stu.setScomputer(a.computer())
    sq.addStudent(stu)
    tocsv.Mysql_csv().red_mysql_to_csv()
    # print(i)
