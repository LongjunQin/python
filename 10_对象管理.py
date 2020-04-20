# 1.创建对象，__new__
# class User:
#     def __init__(self, name):
#         print("初始化方法正在使用。")
#         self.name = name
# u = User("jack")

# class User:
#     def __init__(self, name):
#         print("初始化方法正在使用。")
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         print("__new__方法在使用。")
# u = User("jack")

class User:
    def __init__(self, name):
        print("初始化方法正在使用。")
        self.name = name
    def __new__(cls, *args, **kwargs):
        print("__new__方法在使用。")
        instance = object.__new__(User)
        return instance
u = User("jack")

# 2.del: 删除变量引用，中断连接，元组报错
a = 1
del a
c  = True
del c
l = [1, 2, 3]
del l[0]
d = {'aa': 'aa1', 'bb': 'bb1'}
del d['aa']

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
u1 = User("Jack", 18)
del u1.name

# 3.__del__:类里当对象不被引用时，删除对象
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print("对象被删除")
# u1 = User("Jack", 18)
# # del u1 # 引用被断开，对象被删除
# # print("end")
# # print("--------------------")
# # print("end") # 程序结束后，引用断开，对象被删除
# u2 = u1
# del u1 # 还有u2引用，对象不被删除
# print('end')

# 4.is
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b) # 判断特征是否相等
print(a is b) # 判断地址是否相等，更严格

# 5.单例模式
class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(User)
        return cls.__instance
    
    def __init__(self, name):
        self.name = name
u1 = User("Jack")
u2 = User("Mary")
print(id(u1))
print(id(u2))

"""
6.打印机案例
打印机：添加打印任务，打印
员工：发送打印任务
"""
# class Printer:
#     def __init__(self):
#         self.print_list = []
    
#     def add_msg(self, info):
#         self.print_list.append(info)
    
#     def print_info(self):
#         for i in self.print_list:
#             print(i, end = " ")


# class Staff:
#     def send_msg(self, info, printer):
#         printer.add_msg(info)

# p1 = Printer()
# p2 = Printer()
# s1 = Staff()
# s2 = Staff()
# s1.send_msg("hello", p1)
# print(p1.print_list)
# s2.send_msg("python", p2)
# print(p2.print_list)
# p1.print_info()

# 修改无论创建几个打印机，都是同一台
class Printer:
    __instance = None
    print_list = []
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
        return cls.__instance
    
    def add_msg(self, info):
        Printer.print_list.append(info)
    
    def print_info(self):
        for i in Printer.print_list:
            print(i)


class Staff:
    def send_msg(self, info, printer):
        printer.add_msg(info)

p1 = Printer()

s1 = Staff()
s2 = Staff()
s1.send_msg("hello", p1)
print(p1.print_list)
p2 = Printer()
s2.send_msg("python", p2)
print(p2.print_list)
p1.print_info()

# 创建单例的时候，创建打印列表
class Printer:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
            cls.print_list = []
        return cls.__instance
    
    def add_msg(self, info):
        Printer.print_list.append(info)
    
    def print_info(self):
        for i in Printer.print_list:
            print(i)


class Staff:
    def send_msg(self, info, printer):
        printer.add_msg(info)

p1 = Printer()

s1 = Staff()
s2 = Staff()
s1.send_msg("hello", p1)
print(p1.print_list)
p2 = Printer()
s2.send_msg("python", p2)
print(p2.print_list)
p1.print_info()


# 利用默认参数创建打印列表
class Printer:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
        return cls.__instance
    
    def __init__(self, print_list = []):
        self.print_list = print_list
    
    def add_msg(self, info):
        self.print_list.append(info)
    
    def print_info(self):
        for i in self.print_list:
            print(i)


class Staff:
    def send_msg(self, info, printer):
        printer.add_msg(info)

p1 = Printer()

s1 = Staff()
s2 = Staff()
s1.send_msg("hello", p1)
print(p1.print_list)
p2 = Printer()
s2.send_msg("python", p2)
print(p2.print_list)
p1.print_info()