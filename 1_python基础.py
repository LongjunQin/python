# 1.hello python
print("Hello Python.")
print("Hello World.")

# 2.关于注释
# 单行注释
print("单行注释就是在语句前面加#，mac的快捷键是 command+/") # 单行注释。
# 多行注释
'''
多行注释
就是
在三个引号之间写内容。
'''

# 3.算术运算
'''
+, -, *, /, //, %, **
重点解释摸运算，13除以4得3(//)余1(%).
'''
print(13 // 4)
print(13 % 4)
print(2**3)

# 4.变量：给一个值贴上标签，方便使用，以计算圆面积举例。
# 半径
r = 3
# 圆周率pi
pi = 3.14
# 面积计算
area = pi * r ** 2
# 输出面积结果
print(area)

'''
5.变量类型
int, float, bool, str
'''
print(type(1))
print(type(2.1))
print(type(True))
print(type("Hello Python"))

'''
6.赋值：=, +=, -=...
'''
a = 1
a += 3
print(a)

'''
7.字符串及简单运算
'''
first_name = 'ming'
last_name = 'xiao'
name = first_name + last_name
print(name)
print(name * 5)

'''
8.输入
a1 = input("请输入数字1：")
a2 = input("请输入数字2：")
print(a1 + a2)
'''
# a1 = int(input("请输入数字1："))
# a2 = int(input("请输入数字2："))
# print(a1 + a2)

'''
9. 占位符
%d, %f, %.2f:保留两位小数， %s, %% 
'''
age = 18
height = 1.7867
name = "xiaoming"
print("name: %s, age: %d, height: %.2f" % (name, age, height))

# 10.将圆面积计算改成输入输出格式
# r = int(input("请输入圆半径（单位米）："))
# pi = 3.14
# area = pi * r ** 2
# print("半径是%.2f米的圆面积是：%.4f平方米。" % (r, area))

'''
11.比较运算符：==, !=, >, <, >=, <=
'''
# 数字比较
print(1 == 1)
# 字符串比较，0-9 < A-Z < a<z
print('zhao' < 'qian')

# 关系运算符：and, or, not
print(True and False)
print(1 or False)

