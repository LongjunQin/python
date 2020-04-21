# 1.基本格式
# try:
#     print(a)
# except:    # 错误处理方案
#     print("出错了。")
#
# try:
#     file = open("q.txt", "w")
#     file.read()
# except:
#     print("有问题.")
# finally:
#     file.close()
#     print("成功失败都执行")

# try:
#     print(1)
# except:
#     print("error")
# else:
#     print("不出错我运行")
# finally:
#     print("正常与否我都运行。")

# 2.捕获具体异常
# try:
#     a = 1
#     print(a)
#     b = 1/0
# except NameError:
#     print("没定义变量")
# except ZeroDivisionError:
#     print("除以0了。")
# except Exception:
#     print("未知异常。")

# 3.显示异常详情
# try:
#     a = 1
#     print(a)
#     b = 1/0
# except NameError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print("ZeroDivisionError:" + str(e))
# 异常可以嵌套
try:
    try:
        a = 1
        print(a)
    except NameError as e:
        print(e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:" + str(e))

# 4.抛出异常：检查名字不能和皇帝重名，zhu
# 定义异常类
class NameIsError(Exception):
    pass
# 定义抛出异常方法
def check_name(name):
    if name.find("zhu") != -1:  # 如果找到了zhu
        raise NameIsError("你的名字和皇帝一样了，沙头。")
try:
    check_name("zhuxiaodan")
except NameIsError as e:
    print(e)
else:
    print("名字正常")

"""
5.案例：检查登录
名字长度3-8，英文和数字组成
密码长度6，数字组成
"""
class NameIsError(Exception):
    pass
class PwdIsError(Exception):
    pass

def check_login(name, pwd):
    if len(name) < 3 or len(name) > 8:
        raise NameIsError("名字长度应该在3-8之间。")
    if not name.isalnum():
        raise NameIsError("名字有字母和数字组成。")
    if len(pwd) != 6:
        raise PwdIsError("密码是6位。")
    if not pwd.isdigit():
        raise PwdIsError("密码由数字组成")

try:
    check_login("aaaa","123422")
except NameError as e:
    print(e)
except PwdIsError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("登录成功")
