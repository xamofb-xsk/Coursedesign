import random


class Info:

    def __init__(self):
        self.a1 = ['张', '金', '李', '王', '赵', '郑', '秦', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚',
                   '谢',
                   '邹', '喻', '柏', '水', '窦', '章']
        self.a2 = ['玉', '明', '龙', '芳', '军', '玲', '欣', '刚', '靖', '诗', '默']
        self.a3 = ['', '立', '玲', '', '国', '', '', '涵', '', '妍', '', '楠', '', '凡']

    def xuehao(self):
        a = ['16', '17']
        n = ''
        for i in range(1, 7):
            num = random.randint(0, 9)
            n = n + str(num)
        k = a[random.randint(0, 1)] + n
        return k

    def name(self):
        name = random.choice(self.a1) + random.choice(self.a2) + random.choice(self.a3)
        return name

    def phone(self):
        n = ''
        for i in range(0, 10):
            num = random.randint(0, 9)
            n = n + str(num)
        k = '1' + n
        return k

    def fenshu(self):
        n = ''
        for i in range(0, 4):
            num = random.randint(1, 100)
            n = n + ',' + str(num)
        return n

    def math(self):
        return random.randint(40, 100)

    def english(self):
        return random.randint(40, 100)

    def physical(self):
        return random.randint(40, 100)

    def computer(self):
        return random.randint(40, 100)

    def ginfo(self):
        inf = self.xuehao() + self.name() + self.phone() + self.fenshu() + '\n'
        return inf


a = Info()
f = open('info.csv', 'a+')
s = '学号,姓名,手机,英语,数学,物理,计算机二级\n'
f.write(s)
for i in range(0, 1000):
    info = a.ginfo()
    f.write(info)

f.close()
