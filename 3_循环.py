# 1.演示循环的基本结构
i = 0 # 循环变量从0开始
while i < 5:
    print("Hello Python.")
    i += 1
# 求1-100的和
sum = 0
i = 1
while i <=100:
    sum += i
    i += 1
print("1到100的和是%d." % sum)
# 求1-100的偶数和。
sum = 0
i = 1
while i <=100:
    if i % 2 == 0:
        sum += i
    i += 1
print("1到100的偶数和是%d." % sum)
# 例打印三位回文数，131
# i = 100
# while i < 1000:
#     if i // 100 == i % 10:
#         print(i, end = ',')
#     i += 1

# 2.循环终止与跳出
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# 3.循环嵌套
j = 0
while j < 2:
    i = 0
    while i < 5:
        print(i)
        i += 1
    j += 1
'''
打印星星
*
**
***
****
*****
'''
j = 1
while j < 6:
    i = 0
    while i < j:
        print('*', end = '')
        i += 1
    print()
    j += 1
# 例九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (i, j, i*j), end = '\t')
        i += 1
    print()
    j += 1

# 4.break, continue 只管本循环
j = 1
while j <= 9:
    i = 1
    while i <= j:
        if i == 4:
            break
        print("%d*%d=%d" % (i, j, i*j), end = '\t')
        i += 1
    print()
    j += 1



    