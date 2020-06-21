import menu as menu
import BaseDao as sq
import Student as student
import matplotlib.pyplot as plt
import sqltocsv as tocsv
import pandas as pd
import os
stu = student.Student()

# 得分点3，10%以上的注解
# 添加学生信息
def input_student():
    # 得分点5，使用元组或列表或字典
    info = list()
    sid = input("请输入学号:")
    if not sid:
        print("请输入学号")
    info.append(sid)  # 将学号添加进列表
    name = input("请输入学生姓名:")
    info.append(name)  # 将姓名添加进列表
    phone = input("请输入电话号码:")
    info.append(phone)  # 将电话添加进列表
    english = input("请输入英语成绩:")
    info.append(english)  # 将英语成绩添加进列表
    math = input("请输入数学成绩:")
    info.append(math)  # 将数学成绩添加进列表
    physical = input("请输入物理成绩:")
    info.append(physical)  # 将物理添加进列表
    computer = input("请输入计算机二级成绩:")
    info.append(computer)  # 将计算机二级成绩添加进列表
    stu.setSid(info[0])
    stu.setSname(info[1])
    stu.setSphone(info[2])
    stu.setSenglish(info[3])
    stu.setSmath(info[4])
    stu.setSphysical(info[5])
    stu.setScomputer(info[6])
    sq.addStudent(stu)  # 将数据输入数据库中
    tocsv.Mysql_csv().red_mysql_to_csv()  # 将数据库中的数据导出到csv文件
    print("添加成功")
    input()
    os.system('cls')


# 输出学生信息
def output_student():
    print("学号,姓名,电话,英语,数学,物理,计算机,行数")
    sq.getAll()  # 调用getAll函数将数据库中的数据全部输出
    print("这就是所有的学生信息")
    input()
    os.system('cls')

# 删除学生信息
def delete_student():
    sid = input("请输入要删除的学生学号:")
    stu.setSid(sid)
    sq.delStudent(stu)
    print("删除成功")
    input()
    os.system('cls')

# 修改学生信息
def modify_student_score():
    info = list()
    sid = input("请输入要修改的学生学号:")
    stu.setSid(sid)
    if sq.selectStu(stu) != 0:
        name = input("请输入学生姓名:")
        info.append(name)
        phone = input("请输入电话号码:")
        info.append(phone)
        english = input("请输入英语成绩:")
        info.append(english)
        math = input("请输入数学成绩:")
        info.append(math)
        physical = input("请输入物理成绩:")
        info.append(physical)
        computer = input("请输入计算机成绩:")
        info.append(computer)
        stu.setSname(info[0])
        stu.setSphone(info[1])
        stu.setSenglish(info[2])
        stu.setSmath(info[3])
        stu.setSphysical(info[4])
        stu.setScomputer(info[5])
        sq.updStudent(stu)
    print("修改完成")


# 根据学号查询学生信息
def getsidinfog():
    sid = input("请输入要查询学生的学号:")
    stu.setSid(sid)
    print("学号,姓名,电话,英语,数学,物理,计算机,行数")
    sq.getStudentBySid(stu)
    print("查询成功")
    input()
    os.system('cls')


# 分析学生成绩信息
def analysis():
    # 得分点2，使用matplotlib绘图方法
    df = pd.read_csv("data.csv", encoding='utf_8')  # 读取csv文件并设置编码格式为utf_8
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符
    # 得分点6，使用pandas包，并使用数据切片技术
    math_max = df.数学.max()  # 数学最大值
    english_max = df.英语.max()  # 英语最大值
    physical_max = df.物理.max()  # 物理最大值
    computer_max = df.计算机二级.max()  # 计算机二级最大值

    math_min = df.数学.min()  # 数学最小值
    english_min = df.英语.min()  # 英语最小值
    physical_min = df.物理.min()  # 物理最小值
    computer_min = df.计算机二级.min()  # 计算机二级最小值

    name = df.姓名
    students_scores = df.数学 + df.英语 + df.物理 + df.计算机二级

    math_avg = df.数学.mean()  # 数学平均分
    english_avg = df.英语.mean()  # 英语平均分
    physical_avg = df.物理.mean()  # 物理平均分
    computer_avg = df.计算机二级.mean()  # 计算机二级平均分

    plt.title('学生总成绩分布图')  # 设置直方图名称
    plt.xlabel('学号')  # 设置直方图x轴名
    plt.ylabel('总分')  # 设置直方图y轴名
    plt.bar(name, students_scores)  # 设置直方图条信息
    plt.show()  # 显示直方图

    plt.title('每门课程平均分展示图')  # 设置直方图名称
    plt.xlabel('课程名')  # 设置直方图x轴名
    plt.ylabel('平均分')  # 设置直方图y轴名
    plt.bar('数学', math_avg)  # 设置直方图条信息
    plt.bar('英语', english_avg)  # 设置直方图条信息
    plt.bar('物理', physical_avg)  # 设置直方图条信息
    plt.bar('计算机二级', computer_avg)  # 设置直方图条信息
    plt.show()  # 显示直方图

    plt.title('每门课程最高分展示图')  # 设置直方图名称
    plt.xlabel('课程名')  # 设置直方图x轴名
    plt.ylabel('最高分')  # 设置直方图y轴名
    plt.bar('高数', math_max)  # 设置直方图条信息
    plt.bar('英语', english_max)  # 设置直方图条信息
    plt.bar('物理', physical_max)  # 设置直方图条信息
    plt.bar('计算机二级', computer_max)  # 设置直方图条信息
    plt.show()  # 显示直方图

    plt.title('每门课程最低分展示图')  # 设置直方图名称
    plt.xlabel('课程名')  # 设置直方图x轴名
    plt.ylabel('最低分')  # 设置直方图y轴名
    plt.bar('高数', math_min)  # 设置直方图条信息
    plt.bar('英语', english_min)  # 设置直方图条信息
    plt.bar('物理', physical_min)  # 设置直方图条信息
    plt.bar('计算机二级', computer_min)  # 设置直方图条信息
    plt.show()  # 显示直方图


def main():
    while True:
        menu.show_menu()
        s = input("请选择:")
        if s == 'q':
            return  # 退出
        elif s == '1':
            input_student()
        elif s == '2':
            output_student()
        elif s == '3':
            delete_student()
        elif s == '4':
            modify_student_score()
        elif s == '5':
            getsidinfog()
        elif s == '6':
            analysis()


main()  # 从主函数开始
