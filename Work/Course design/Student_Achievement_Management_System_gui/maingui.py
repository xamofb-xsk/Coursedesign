from tkinter import *
import tkinter.ttk as ttk
import os
from tkinter.messagebox import *
import Student_Achievement_Management_System_gui.detailgui as dt
import Student_Achievement_Management_System_gui.rpass as ps


class Main_Windows(Tk):
    """
    主窗体的构造函数
        1. current_user,current_time的引入是为了加载logingui.py窗体中用户输入及加载登录时间记录时间的参数
        2. 同样设计主窗体下界面的布局及配置
    """

    def __init__(self, current_login_user, current_time):  # current_login_user为了实现登录信息的加载（记录logingui界面中当前用户是谁）
        # current_time同样是为了记录当前用户登录的系统时间
        super().__init__()
        self.title("主窗体")
        self.geometry("1200x700+1+20")  # 通过控制图像大小可以通过+号来调整窗体出现的位置
        self.resizable(0, 0)  # 固定窗体大小.不允许改动窗体大小. resizable(0,0)表示x轴为0y轴也为0
        self.iconbitmap(
            R"C:\Users\Administrator\PycharmProjects\untitled1\wangzhexiagu\GUI_student_system\photo\china.ico")  # 加载.ico文件到窗口小图标. 网上可以将png转成ico文件
        # 添加图片背景色
        self["bg"] = "RoyalBlue"

        # 设置全局变量
        self.login_times = current_time  # 为了记录用户的登录时间
        self.all_list = []  # 读取student_info.txt中所有的元素并存入all_list中
        self.current_stu_list = []  # 存储双击行匹配到的最终数据
        self.get_number_result = []  # 用户存储获取到的所有学员信息
        self.file_path = R"C:\Users\Administrator\PycharmProjects\untitled1\wangzhexiagu\GUI_student_system\loginUserInfo_Data\student_info.txt"
        self.action_flag = 0  # 设置查看/修改/添加学生信息的title值,默认为0
        self.current_user_list = current_login_user  # 把login界面的list传到主界面接收

        # 加载窗体
        self.Setup_UI()

        # 自动执行函数
        self.Load_local_Data()  # 自动加载数据（加载的是all_list中已经读取到的所有数据）
        self.load_TreeView(self.all_list)  # 自动将all_list中每一行的数据加载到TreeView中展示

        # 将窗体的行为转化为方法
        self.protocol("WM_DELETE_WINDOW", self.close_windows)  # "WM_DELETE_WINDOW"为固定写法

    def Setup_UI(self):
        """
        布局主窗体的窗体并对其中的控件属性进行配置
        :return:
        """
        # 设置Sytle配置控件的属性
        self.Style01 = ttk.Style()
        self.Style01.configure("left.TPanedwindow", background="RoyalBlue")
        self.Style01.configure("right.TPanedwindow", background="skyblue")
        self.Style01.configure("TButton", font=("微软雅黑", 12, "bold"))
        self.Style01.configure("TLabel", font=("微软雅黑", 10, "bold"))
        self.Style01.configure("labframe.TButton", font=("微软雅黑", 10, "bold"))
        self.Style01.configure("title1.TLabel", font=("微软雅黑", 10, "bold"), background="lightblue")

        # 加载窗体图片
        self.login_img = PhotoImage(
            file=R"C:\Users\Administrator\PycharmProjects\untitled1\wangzhexiagu\GUI_student_system\photo\1.png")
        self.label_img = ttk.Label(self, image=self.login_img)
        self.label_img.pack()

        # 加载当前用户和时间
        self.label_login_user = ttk.Label(self, text="当前登录用户:" + str(self.current_user_list[0]).title() +
                                                     "\n登录时间:" + self.login_times, style="title1.TLabel")
        # str(self.current_user_list[0]).title()为用户登录后的首字母显示未大写

        self.label_login_user.place(x=1000, y=165)

        # 左边按钮区域的布局
        self.pan_left = ttk.PanedWindow(width=200, height=500, style="left.TPanedwindow")
        self.pan_left.pack(side=LEFT, padx=3, pady=1)

        # 添加左边区域按钮
        self.buttion_useradd = ttk.Button(self.pan_left, text="添加学生", width=12, command=self.add_student)
        self.buttion_useradd.place(x=30, y=20)

        self.buttion_userupdate = ttk.Button(self.pan_left, text="修改学生", width=12, command=self.update_student)
        self.buttion_userupdate.place(x=30, y=60)

        self.buttion_userdelete = ttk.Button(self.pan_left, text="删除学生", width=12, command=self.delete_student)
        self.buttion_userdelete.place(x=30, y=100)

        self.buttion_changepassword = ttk.Button(self.pan_left, text="更改密码", width=12,
                                                 command=self.change_password_windows)
        self.buttion_changepassword.place(x=30, y=140)

        # 右边按钮区域的布局
        self.pan_right = ttk.PanedWindow(width=991, height=500, style="right.TPanedwindow")
        self.pan_right.pack(side=LEFT)

        # 添加查询区域(属于右边区域)
        self.labelFrame_query = ttk.LabelFrame(self.pan_right, text="学生信息", width=990, height=60)
        self.labelFrame_query.place(x=1, y=1)

        # 添加控件
        self.label_number = ttk.Label(self.labelFrame_query, text="学号:")
        self.label_stu_no = StringVar()
        self.label_number.place(x=10, y=10)
        self.entry_number = ttk.Entry(self.labelFrame_query, textvariable=self.label_stu_no, font=("微软雅黑", 10, "bold"),
                                      width=8)
        self.entry_number.place(x=50, y=10)

        self.label_name = ttk.Label(self.labelFrame_query, text="姓名:")
        self.get_stu_name = StringVar()
        self.label_stu_name = StringVar()
        self.label_name.place(x=130, y=10)

        self.entry_name = ttk.Entry(self.labelFrame_query, textvariable=self.get_stu_name, font=("微软雅黑", 10, "bold"),
                                    width=10)
        self.entry_name.place(x=170, y=10)

        self.label_age = ttk.Label(self.labelFrame_query, text="年龄:")
        self.get_stu_age = StringVar()
        self.label_age.place(x=270, y=10)
        self.entry_age = ttk.Entry(self.labelFrame_query, textvariable=self.get_stu_age, font=("微软雅黑", 10, "bold"),
                                   width=5)
        self.entry_age.place(x=310, y=10)

        self.label_mobile = ttk.Label(self.labelFrame_query, text="电话:")
        self.get_stu_mobile = StringVar()
        self.label_mobile.place(x=360, y=10)
        self.entry_mobile = ttk.Entry(self.labelFrame_query, textvariable=self.get_stu_mobile,
                                      font=("微软雅黑", 10, "bold"), width=16)
        self.entry_mobile.place(x=400, y=10)

        self.label_address = ttk.Label(self.labelFrame_query, text="住址:")
        self.get_stu_address = StringVar()
        self.label_address.place(x=540, y=10)
        self.entry_address = ttk.Entry(self.labelFrame_query, textvariable=self.get_stu_address,
                                       font=("微软雅黑", 10, "bold"), width=20)
        self.entry_address.place(x=590, y=10)

        self.button_search = ttk.Button(self.labelFrame_query, text="查询", width=6, style="labframe.TButton",
                                        command=self.get_student_result)
        self.button_search.place(x=780, y=10)

        self.button_homepage = ttk.Button(self.labelFrame_query, text="返回主页面", width=10, style="labframe.TButton"
                                          , command=self.load_all_data)
        self.button_homepage.place(x=850, y=10)

        # 添加TreeView控件
        self.treeView = ttk.Treeview(self.pan_right, columns=("学号", "姓名", "年龄", "性别", "电话", "邮箱", "家庭住址"),
                                     show="headings")
        # 设置每一列的宽度和对齐方式
        self.treeView.column("学号", width=80, anchor="center")
        self.treeView.column("姓名", width=60, anchor="w")  # w代表西面也就是左边对齐的意思
        self.treeView.column("年龄", width=60, anchor="center")
        self.treeView.column("性别", width=60, anchor="center")
        self.treeView.column("电话", width=180, anchor="center")
        self.treeView.column("邮箱", width=250, anchor="center")
        self.treeView.column("家庭住址", width=298, anchor="w")

        # 设置表头的标题文本
        self.treeView.heading("学号", text="学号")
        self.treeView.heading("姓名", text="姓名")
        self.treeView.heading("年龄", text="年龄")
        self.treeView.heading("性别", text="性别")
        self.treeView.heading("电话", text="电话")
        self.treeView.heading("邮箱", text="邮箱")
        self.treeView.heading("家庭住址", text="家庭住址")

        # 插入滚动条
        # self.scrollBar = Scrollbar(self)
        # self.scrollBar.pack(side=RIGHT,fill=Y)

        # 设置关联
        # self.scrollBar.config(command = self.treeView.yview)

        # 展示treeView信息
        self.treeView.place(x=1, y=60, height=450)

        # 双击TreeView中某一行触发PopUp窗体
        self.treeView.bind("<Double-1>", self.view_student)  # <Double>是必须的Double以后的可以任意但是不能跟命令行重名

    def Load_local_Data(self):
        """
        加载student_info.txt中的信息(本地文件的读取)
        :return: 把文件中的每一个元素存储到 all_list 中
        """
        if not os.path.exists(self.file_path):
            showinfo("系统提示", "文件不存在.请确认后重新加载!!")
        else:
            try:
                with open(self.file_path, mode="r") as fd:
                    current_list = fd.readline()  # 一次读一行
                    while current_list:  # 表示直到current_list中所有元素被读完，循环结束
                        temp_list = current_list.split(",")  # 按照逗号把每个list中的元素分割出来
                        self.all_list.append(temp_list)  # 把分割后的每个元素重新添加到all_list列表中
                        current_list = fd.readline()  # 因为我们一次只读一行。读完后如果不加这一句那么循环会一直只读第一行。

            except:
                showinfo("系统信息", "文件读取出现异常.请联系管理员！！")

    def load_TreeView(self, student_list: list):
        """
        1. 判断all_list中的长度是否为0如果为0则没有数据被加载
        2. 把数据加载到treeView中
        :return:
        """
        # 加载数据后清空TreeView
        for i in self.treeView.get_children():  # 固定用法
            self.treeView.delete(i)

        # 加载数据
        if len(student_list) == 0:  # 这里的student_list是个参数变量传什么数据就是什么。这里最终传的事all_list中的数据在load_TreeView(self.all_list)中展示
            showinfo("系统消息", "没有数据被加载！")
        else:
            for index in range(len(student_list)):
                self.treeView.insert("", index, values=student_list[index])

    def get_student_result(self):
        """
        1. 获取输入的值
        2. 判断如果输入的值包含在all_list中那么把数据存入到get_number_result列表中
        :return:
        返回的是匹配到的学生编号的所有信息
        """
        # 清空get_number_result中的数据(因为每次查询一个stu_number就显示一条.如果不清空就会每次查询的结果都会被显示)
        self.get_number_result.clear()

        # 获取输入的值
        get_input = []
        get_input.append(self.label_stu_no.get().strip())
        get_input.append(self.get_stu_name.get().strip())
        get_input.append(self.get_stu_age.get().strip())
        get_input.append(self.get_stu_mobile.get().strip())
        get_input.append(self.get_stu_address.get().strip())

        # print(get_input)

        # 匹配学号把结果存入到get_number_result中(第一个元素学号必须填写)
        for item in self.all_list:
            if get_input[0] in item[0] and get_input[1] in item[1] and get_input[2] in item[2] \
                    and get_input[3] in item[4] and get_input[4] in item[6]:
                self.get_number_result.append(item)
        # print(self.get_number_result)

        # 把数据加载到TreeView中
        self.load_TreeView(self.get_number_result)

    def load_all_data(self):
        """
        重新加载一下treeView中的所有数据就是展开全部信息
        :return:
        """
        # 清空所有填写的内容文本框
        self.label_stu_no.set("")
        self.get_stu_name.set("")
        self.get_stu_age.set("")
        self.get_stu_mobile.set("")
        self.get_stu_address.set("")

        # 把all_list中的数据加载到TreeView
        self.load_TreeView(self.all_list)

    def load_detail_windows(self):
        """
        创建load_detail_windows方法调用class detailgui模块中的方法（加载学生明细窗体）
        :return:
        """
        detail_window = dt.Detail_Windows(self.action_flag, self.current_stu_list,
                                          self.all_list)  # detailgui中传了几个参数就要load的几个参数
        self.wait_window(detail_window)  # 通过self.wait_window()方法接收detail_window的值
        return detail_window.comp_info

    def add_student(self):
        self.action_flag = 2  # 如果action_flag值等于2则title值为添加学生信息
        if self.load_detail_windows() == 1:
            self.load_all_data()
        else:
            return

    def update_student(self):
        self.action_flag = 3  # 如果action_flag值等于3则title值为修改学生信息
        # 获取双击行的数据
        item = self.treeView.selection()[0]
        temp_stu_list = self.treeView.item(item, "values")

        # 因为双击行中的数据并不是我们想要的所有数据，因此我们还要遍历all_list中的元素。通过双击行获取的学号跟all_list中的学号做对比
        # 如果两个学号相等那么把all_list中对等的那一行的所有item存入到预备号的current_stu_list中
        for item in self.all_list:
            if item[0] == temp_stu_list[0]:
                self.current_stu_list = item

        # 加载数据
        if self.load_detail_windows() == 1:
            self.load_all_data()
        else:
            return

    def view_student(self, event):
        """
        1.获取选定行的数据
        2.遍历所有学员信息,当前学员学号等于所有学员信息中学号的信息那么就读取选定行所有数据
        3.重新加载数据
        :param event:
        :return:
        """
        self.action_flag = 1  # 如果action_flag值等于1则title值为查看学生信息
        # 固定方法获取双击行的数据
        item = self.treeView.selection()[0]
        temp_stu_list = self.treeView.item(item, "values")

        # 因为双击行中的数据并不是我们想要的所有数据，因此我们还要遍历all_list中的元素。通过双击行获取的学号跟all_list中的学号做对比
        # 如果两个学号相等那么把all_list中对等的那一行的所有item存入到预备号的current_stu_list中
        for item in self.all_list:
            if item[0] == temp_stu_list[0]:
                self.current_stu_list = item
        self.load_detail_windows()

    def delete_student(self):
        # 获取选中行的数据
        item = self.treeView.selection()[0]
        temp_stu_list = self.treeView.item(item, "values")

        # 提醒是否删除数据

        choose = askyesno("删除确认", "确定要删除学生信息【学号:" + temp_stu_list[0] + "  姓名:" + temp_stu_list[1] + " ] 信息吗？")

        if choose:
            # 如果是执行下面代码
            for index in range(len(self.all_list)):
                if self.all_list[index][0] == temp_stu_list[0]:
                    self.all_list.pop(index)
                    break
            # 更新表格
            self.load_all_data()
            showinfo("系统消息", "数据删除成功！")

        else:
            return

    def close_windows(self):
        """
        1.提醒用户关闭窗口前是否保存数据
        2.保存数居前先清空数据再保存数据
        :return:
        """
        choose = askyesno("系统关闭提醒", "是否将修改的数据保存到文件？")
        if choose:
            try:
                with open(self.file_path, mode="w") as fd:
                    fd.write("")
                with open(self.file_path, mode="a") as fd:
                    for item in self.all_list:
                        temp = ",".join(item)
                        temp = temp.replace("\n", "") + "\n"  # 为了让光标换行
                        fd.write(temp)
            except:
                showinfo("系统消息", "写入文件出错！")

            # 提醒
            showinfo("系统消息", "文件写入成功！")

            # 关闭窗体
            self.destroy()
        else:
            self.destroy()

    def change_password_windows(self):
        this_password_windows = ps.change_User_password(self.current_user_list)
        # 把list绑定到change_password_windows中


if __name__ == "__main__":
    this_main_window = Main_Windows()
    this_main_window.mainloop()

用户登录主界面
