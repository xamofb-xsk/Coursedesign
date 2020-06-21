# #字符串比较大小
str1 = input("请输入第一个字符串")
str2 = input("请输入第二个字符串")
if str1 > str2:
    print("第一个字符串大")
elif str1 == str2:
    print("两个字符串一样大")
else:
    print("第二个字符串比较大")
# #字符串逆输出
str = input("请输入字符串")
print(str[::-1])
# # #汉诺塔
def move(n, a, b, c):
    if n == 1:  # 递归的收敛条件,当n为1,时,执行移动的操作
        print('move:', a, '-->', c)  # 打印 move 为字符串,a和c是参数
        return
    move(n - 1, a, c, b)  # 先把n-1个盘子,从a移动到b
    move(1, a, b, c)  # 再将剩下的1个盘子,从a移动到c
    move(n - 1, b, a, c)  # 柱子b上面有n-1个盘子,再将盘子从b,借助a,移动到c


move(3, 'A', 'B', 'C')