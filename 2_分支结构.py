# 1.if 结构
# 判断一个数是否大于100
num = 199
if num > 100:
    print("%.2f大于100" % num)
# 判断一个数是三位的偶数
num = 420
if num % 2 ==0 and num > 99 and num < 1000:
    print("%d是三位偶数。" % num)

# 2.if else
# 判断偶数
num = 19
if num % 2 == 0:
    print("%d是偶数。" % num)
else:
    print("%d是奇数。" % num)

# 3.if else elif
# 判断考试结果
score = 95
if score >= 90:
    print("A")
elif score >=80 and score < 90:
    print("B")
else:
    print("C")
# 减肥计划
# day = int(input("今天是星期几："))
# if day == 1:
#     print("runing.")
# elif day == 2:
#     print("biking.")
# elif day == 3:
#     print("swimming.")
# elif day == 4:
#     print("boxing.")
# elif day == 5:
#     print("climbing")
# else:
#     print("resting.")

# 4.嵌套分支语句：判断奇偶正负。
num = 35
if num > 0:
    if num % 2 == 0:
        print("%d是正偶数。" % num)
    else:
        print("%d是正奇数。" % num)
else:
    if num % 2 == 0:
        print("%d是负偶数。" % num)
    else:
        print("%d是负奇数。" % num)
'''
外卖结算，满30减10，满50减20，满100减50，会员再8折。
'''
price = int(input("How much:"))
m = input("是否是会员（y/n）：")

if price >= 100:
    price -= 50
elif price >= 50:
    price -= 20
elif price >= 30:
    price -= 10
if m == "y":
    price *= 0.8
print("你需要付费%.2f元" % price)

# 6.超长句：\进行断句
print("Hello World. Hello World. Hello World. Hello World. \
Hello World. Hello World. Hello World. Hello World. Hello World. \
Hello World. Hello World. Hello World. Hello World. Hello World. \
Hello World. Hello World. Hello World. Hello World. ")





