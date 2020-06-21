# 导入 tkinter 库
from tkinter import *
# 导入tkinter库中的ttk
from tkinter import ttk
# 导入com.zs.dao下的BaseDao模块
import BaseDao as bd
# 导入com.zs.entity下的Student实体类
import Student as s
# 导入tkinter的对话框
from tkinter import messagebox

# 实例化学生实体类
stu = s.Student()
# 底部容器的右边按钮绑定的方法
# 添加
def insert():
    # 获取输入框的值
    snameValue = snameEntry.get()
    ssidValue = sidEntry.get()
    sphoneValue = sphoneEntry.get()
    saddressValue = saddressEntry.get()

    if snameValue == "" or ssidValue == "" or sphoneValue == "" or saddressValue == "":
        messagebox.showwarning("警告", "学生的学号、姓名、电话、住址不能为空！")
    else:
        print("添加中......")
        stu.setSaddress(saddressValue)
        stu.setSname(snameValue)
        stu.setSphone(sphoneValue)
        stu.setSid(ssidValue)
        bd.addStudent(stu)
        # 添加之后重新加载表格数据
        fresh()
        clearEntry()
        print("添加成功！")


# 删除
def delete():
    sidValue = sidEntry.get()
    if sidValue != "":
        print("删除中......")
        sidValue = sidEntry.get()
        stu.setSid(sidValue)
        print(sidValue)
        bd.delStudent(stu)
        # 删除之后刷新数据
        fresh()
        # 清空输入框
        clearEntry()
        print("删除成功！")
    elif sidValue == "":
        # 用户没有选择任何学生进行删除
        messagebox.showinfo("提示", "请输入学生学号以删除")


# 修改
def update():
    sidValue = sidEntry.get()
    if sidValue != "":
        print("修改中......")
        sidValue = sidEntry.get()
        snameValue = snameEntry.get()
        sphoneValue = sphoneEntry.get()
        saddressValue = saddressEntry.get()

        stu.setSid(sidValue)
        stu.setSname(snameValue)
        stu.setSphone(sphoneValue)
        stu.setSaddress(saddressValue)
        bd.updStudent(stu)
        fresh()
        clearEntry()
        print("修改成功！")
    elif sidValue == "":
        # 用户没有选择任何学生进行修改
        messagebox.showwarning("警告", "请选择需要修改的学生")


# 查询
def select():
    print("查询中......")
    sidValue = sidEntry.get()
    if sidValue != "":
        sidValue = sidEntry.get()
    snameValue = snameEntry.get()
    sphoneValue = sphoneEntry.get()
    saddressValue = saddressEntry.get()
    if saddressValue != "":
        saddressValue = saddressEntry.get()

    stu.setSid(sidValue)
    stu.setSname(snameValue)
    stu.setSphone(sphoneValue)
    stu.setSaddress(saddressValue)

    for i in treeView.get_children():
        treeView.delete(i)
    for i in bd.selectStu(stu):
        treeView.insert("", 0, values=(i[0], i[1], i[2], i[3]))
    print("查询成功......")


# 刷新数据的方法
def fresh():
    for i in treeView.get_children():
        treeView.delete(i)
    for i in bd.getAll():
        treeView.insert("", 0, values=(i[0], i[1], i[2], i[3]))


# 表格选中某列的方法
def treeViewSelect(event):
    item = treeView.selection()
    itemValues = treeView.item(item, "values")
    sidValue = itemValues[0]
    snameValue = itemValues[1]
    sphoneValue = itemValues[2]
    saddressValue = itemValues[3]
    # 默认清空
    clearEntry()
    # 赋值
    sidEntry.insert(0, sidValue)
    snameEntry.insert(0, snameValue)
    sphoneEntry.insert(0, sphoneValue)
    saddressEntry.insert(0, saddressValue)


# 清空输入框的值
def clearEntry():
    sidEntry.delete(0, END)
    snameEntry.delete(0, END)
    sphoneEntry.delete(0, END)
    saddressEntry.delete(0, END)


# 实例化一个新窗口
tk = Tk()

# 设置窗口大小
tk.geometry("600x380")

# 设置窗口的标题
tk.title("学生管理系统\n")

# 在窗口中添加标签
label = Label(tk, text="欢迎使用学生管理系统！", bg="#0078D7", fg="black", font=("宋体", 18))

# 标签出现在窗口的位置
label.pack(side=TOP, fill="x")

# 在窗口中添加数据展示
# 设置show属性为 headings 即可隐藏首列
treeView = ttk.Treeview(tk, show="headings", column=("sid", "sname", "sphone", "saddress"))

# 数据列表设置属性
treeView.column("sid", width=150, anchor="center")
treeView.column("sname", width=150, anchor="center")
treeView.column("sphone", width=150, anchor="center")
treeView.column("saddress", width=150, anchor="center")

# 设置表头
treeView.heading("sid", text="学号")
treeView.heading("sname", text="姓名")
treeView.heading("sphone", text="电话")
treeView.heading("saddress", text="住址")

# 初始化加载表格的数据
fresh()

# 实例化底部大容器
bottomFrame = Frame(tk)

# 实例化底部大容器中的左右两个容器
leftFrame = Frame(bottomFrame)
rightFrame = Frame(bottomFrame)

# 左边容器
sidLadel = Label(leftFrame, text="学号：")
sidEntry = Entry(leftFrame)

snameLadel = Label(leftFrame, text="姓名：")
snameEntry = Entry(leftFrame)

saddressLadel = Label(leftFrame, text="电话：")
saddressEntry = Entry(leftFrame)

sphoneLadel = Label(leftFrame, text="住址：")
sphoneEntry = Entry(leftFrame)

sidLadel.grid(row=0, column=0)
sidEntry.grid(row=0, column=1)

snameLadel.grid(row=0, column=2)
snameEntry.grid(row=0, column=3)

saddressLadel.grid(row=1, column=0)
saddressEntry.grid(row=1, column=1)

sphoneLadel.grid(row=1, column=2)
sphoneEntry.grid(row=1, column=3)

# 右边容器
insertBtn = Button(rightFrame, text="添加", command=insert)
deleteBtn = Button(rightFrame, text="删除", command=delete)
updateBtn = Button(rightFrame, text="修改", command=update)
selectBtn = Button(rightFrame, text="查询", command=select)
insertBtn.grid(row=0, column=0)
deleteBtn.grid(row=0, column=1)
updateBtn.grid(row=1, column=0)
selectBtn.grid(row=1, column=1)

# 底部的【一键清空】按钮
clearButton = Button(text="一键清空", command=clearEntry)

# 给TreeView添加点击事件
treeView.bind("<<TreeviewSelect>>", treeViewSelect)

# 显示表的信息
treeView.pack()

# 显示左右容器
leftFrame.pack(side=LEFT)
rightFrame.pack(side=RIGHT)

# 显示底部大容器
bottomFrame.pack()

# 显示底部的【一键清空】按钮
clearButton.pack()

# 获取电脑屏幕的宽度和高度
winWidth = tk.winfo_screenwidth()
winHeight = tk.winfo_screenheight()

# 窗口的宽度
tkWidth = 600
tkHeight = 380

# 居中的px
x = (winWidth - tkWidth) / 2
y = (winHeight - tkHeight) / 2

tk.geometry("%dx%d+%d+%d" % (tkWidth, tkHeight, x, y))
# 进入消息循环
tk.mainloop()
