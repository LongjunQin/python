# 1.函数定义与调用
def say():
    print("Hello World.")
    print("Hello Python.")
say()

# 2.函数注释
def say():
    """
    函数功能：打招呼
    """
    print("Hello World.")
    print("Hello Python.")
say()

# 3.函数参数
# 一个参数，求1到n的和
def sum_n(n): # 形参
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    print(sum)
sum_n(3) # 实参
# 多个参数，求两个数和
def add_2(a, b):
    print(a+b)
add_2(1, 4)
# 例找两个数最大值
def max2(a, b):
    if a >= b:
        print(a)
    else:
        print(b)
max2(4, 10)

# 4.函数作用域：局部变量仅做用局部且在局部优先级高于全局变量，函数内想使用全局变量，先声明 global，再使用。
def max2(a, b):
    x = 10
    print("局部变量：%f" % x)
    if a >= b:
        print(a)
    else:
        print(b)
x = 20
max2(1,2)
print("全局变量：%f" % x)
# global
def max2(a, b):
    global x
    x = 10
    print("局部变量：%f" % x)
    if a >= b:
        print(a)
    else:
        print(b)
x = 20
max2(1,2)
print("全局变量：%f" % x)

# 5.返回值 return，遇到return就语句结束。改造最大值函数
def max2(a, b):
    if a >= b:
        return a
    else:
        return b
value = max(3, 4)
print("最大值是%.2f。" % value)
# return返回多个值
def test():
    return 1, 2, 3
a, b, c = test()
print("多个返回值：%d, %d, %d" % (a, b, c))
# 6.函数间调用
def add2(a, b):
    return a + b
def div2(a, b):
    return a / b

def test(a, b):
    return add2(a, b) / div2(a, b)
print(test(1, 2))
'''
求三个数最大值，要求：
利用两个数最大值函数
获得返回值
'''
def max2(a, b):
    if a >= b:
        return a
    else:
        return b
def max3(a, b, c):
    temp = max2(a, b)
    result = max(temp, c)
    return result
result = max3(3, 70, 5)
print("最大值是%d" % result)
