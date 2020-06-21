def input_student():
    infos = []
    while True:
        n = input("请输入学生姓名:")
        if not n:
            break
        a = int(input("请输入年龄:"))
        s = int(input("请输入成绩:"))
        d = {'name': n, 'age': a, 'score': s}  # d=dict(name=n,age=a,score=s)
        infos.append(d)  # 将字典数据添加到列表中
    return infos


# 显示信息
def output_student(L):
    print("+------------+------------+------------+")
    print("|    姓名    |    年龄    |    成绩    |")
    print("+------------+------------+------------+")
    for d in L:  # 绑定字典
        n = d['name']
        a = d['age']
        s = d['score']
        n = str(n)
        a = str(a)  # 将整型转换成字符串
        s = str(s)
        print("|" + n.center(12) + "|" + a.center(12) + "|" + s.center(12) + "|")
    print("+------------+------------+------------+")


# 删除信息
def delete_student(L):
    name = input(print("请输入要删除的学生姓名:"))
    i = 0
    while i < len(L):
        if L[i]['name'] == name:
            del L[i]
            print("学生" + name + "删除成功")
            return True
        elif i >= len(L) - 1:
            print("学生" + name + "不存在")
            return False
        i += 1


# 修改学生成绩
def modify_student_score(L):
    n = input("请输入要修改的学生姓名:")
    i = 0
    while i < len(L):
        if L[i]['name'] == n:
            L[i]['score'] = input("请输入新成绩:")
            print("修改成绩ＯＫ")
            return True
        elif i >= len(L) - 1:
            print(n + "学生不存在，不能修改")
            return False
        i += 1


# by学生成绩排序
def output_student_score_desc(L):
    lis = sorted(L, key=lambda d: d['score'], reverse=True)
    output_student(lis)


def output_student_score_asc(L):
    lis = sorted(L, key=lambda d: d['score'], reverse=False)
    output_student(lis)


# by学生年龄排序
def output_student_age_desc(L):
    lis = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(lis)


def output_student_age_asc(L):
    lis = sorted(L, key=lambda d: d['age'], reverse=False)
    output_student(lis)
# 解释说明:
# sorted(iterable,key=None,reverse=False) 函数作用是将原可迭代对象排序，生成新的列表
# 单步测试
# l=[]
# l+=input_student()
# output_student(l)
