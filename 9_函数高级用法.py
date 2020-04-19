# 1.默认参数
def test(a = 5, b = 6):
    print(a)
    print(b)

test()

def test(a, b = 100, c = 200): # 默认参数在参数后面，按顺序赋值，不可跳跃
    print(a)
    print(b)
    print(c)

test(1, 2)
# 默认参数案例
s = "Helle World."
print(s.index('e'))
print(s.index('e', 2, 8))
l = [1, 2, 3]
print(l.pop(0))
print(l.pop())
'''
parameter: 形参
argument: 实参
'''

# 2.关键字参数：针对调用时
def test(a=200, b=100):
    print(a)
    print(b)

test(b=1) # 解决默认参数的跳跃赋值
# 案例
print("Hello World.", end = "___")

# 3.可变参数：一个形参接受任意多个参数，只出现一次，在参数后面， 关键词参数前面
def sum(a, *args):
    print(a)
    print(args) # 元组
    print(*args) # 自动拆包
sum(1,2,3,4,5)

def sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(sum(1,2,3,4,5))
# 案例：可变参数在关键字参数前面
print("a", "b", "c", sep = '*') # print的第一个参数是可变参数，*values，后面跟着的是默认参数，end, sep

# 4.字典参数：接受不被接受的关键字参数
def test(**kwargs):
    print(kwargs) # {'a': 1, 'b': 2}
    print(*kwargs) # 将字典拆包，得到键
    #print(**kwargs) # 就是原本传入的关键字参数：a = 1, b = 2
test(a = 1, b = 2)

def test(a, *args, b = 1, **kwargs): # 参数顺序，位置参数，可变参数，默认参数，字典参数
    pass

# 案例：多层级调用
"""
流水线作业
对字符两端去空格，小写转大写
按空格切字符串，输出字符串，在同行，用：分割
"""
s = '  Hello Wrold Hello Python    '

def step2(s):
    s = s.split()
    for i in s:
        print(i, end=": ")

def step1(s):
    s = s.strip()
    s = s.upper()
    step2(s)
step1(s)

# 改进成用任意分隔符或者其他输出格式
s = '  Hello Wrold Hello Python    '

def step2(s, **kwargs): # 字典变量在函数间传递关键字函数同时不做处理
    s = s.split()
    for i in s:
        print(i, **kwargs)

def step1(s, **kwargs):
    s = s.strip()
    s = s.upper()
    step2(s, **kwargs)
step1(s, end="&&&&&&")

#  案例2
# 原函数层级
def call_depth_1(a = 10):
    print("call_depth_1: a = %d" % a)
    call_depth_2()

def call_depth_2(b = 20):
    print("call_depth_2: b = %d" % b)
    call_depth_3()

def call_depth_3(c = 30):
    print("call_depth_3: c = %d" % c)
    call_depth_4()

def call_depth_4(d = 40):
    print("call_depth_4: d = %d" % d)
call_depth_1()

# 改进，通过第一个函数，给所有函数重新传参
def call_depth_1(a = 10, **kwargs):
    print("call_depth_1: a = %d" % a)
    call_depth_2(**kwargs)

def call_depth_2(b = 20, **kwargs):
    print("call_depth_2: b = %d" % b)
    call_depth_3(**kwargs)

def call_depth_3(c = 30, **kwargs):
    print("call_depth_3: c = %d" % c)
    call_depth_4(**kwargs)

def call_depth_4(d = 40, **kwargs):
    print("call_depth_4: d = %d" % d)
call_depth_1(a = 1, b = 2, c = 3, d = 4)

# *的小结
def test(**kwargs):
    print(kwargs)
    print(*kwargs) # *就是自动拆包，字典的自动拆包就是获得键
    # print(**kwargs) 两个*就是以实参的形式传进来，a=1, b=2，print报错
test(a=1, b=2)

l = [1, 2]
t = (1, 2)
s = {1, 2}
d = {'aa': 'aa1', 'bb': "bb1"}
str = 'He'
print(*l)
a,b = l # 自动拆包
print(a)
print(b)
a, b = t
print(a)
print(b)
a, b = s
print(a)
print(b)
a, b = d # 自动拆包只拆键
print(a)
print(b)
a, b = str
print(a)
print(b)

def test():
    return 1, 2 # 自动组包

a = test()
print(a)
a, b = test() # 自动拆包
print(a)

"""
5.函数调用
递归函数，最好别用
就1-100的和
"""
def sum(n):
    if n == 1: # 有明确的结束标志
        return 1
    else:
        return sum(n-1) + n 
print(sum(100)) # 最多一千层，本身调用也算一层

# 6.lambda
add = lambda a, b: a+b
print(add(1,2))
result = (lambda a, b: a + b)(1, 2)
print(result)
# 无参数：可以
print((lambda : "hello")()) # 括号不能删
# 多返回值
print((lambda : (2, 3))()) # 不可以，不能自动组包，只能手动组包变成一个元组
# 无返回值，就返回None
print((lambda a, b: print("hello"))(1,2)) # print()无返回值，没有return，就返回None, return就自动组包，接受时自动解包
# 数值存储模型
print((lambda : [i**2 for i in range(100) if i % 2 == 0 and i % 7 == 0])())










