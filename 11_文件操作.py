# 1.文件的打开
# 方式一
file = open("232.txt", "w")
file.write("Hello Python.")
file.close()
# 方式二
with open("type2.txt", "w") as file:
    file.write("Hello World.")

'''
2.读写模式：
a:追加，r：读，w：写
ab,wb,rb：二进制读写，更安全，推荐
r+, a+, w+ 读写都行
rb+, ab+, wb+ 
'''
with open("232.txt", "a") as file:
    file.write("Hello Python. Hello World.")

with open("232.txt", "r") as file:
    info = file.read()
    print(info)

# 3.操作文件
with open("1.txt", "w") as file:
    file.write("Hello Python")

file = open("1.txt", "r")
while True:
    info = file.read(1024)  # 防止内存溢出，一般一次读1k=1024
    if len(info) != 0:  # 结束标志是读到空字符串，""
        print(info)
    else:
        break
file.close()

# 复制图片等其他文件
# file_old = open("Python.xlsx", "rb")
# file_new = open("Python_new.xlsx", "wb")
# while True:
#     info = file_old.read(1024)
#     if len(info) != 0:
#         file_new.write(info)
#     else:
#         break
# file_old.close()
# file_new.close()




with open("1.txt", "r") as file:
    while True:
        info = file.read(4)
        if len(info) != 0:
            print(info)
        else:
            break


with open("1.txt", "r") as file:
    while True:
        info = file.readline()  # 一次读一行
        if len(info) != 0:
            print(info)
        else:
            break

with open("1.txt", "r") as file:
    info = file.readlines()  # 将文件每行作为一个元素，放入列表
    print(info)

with open("3.txt", "w") as file:
    file.writelines(["whllo\n", "python\n", "world\n"])  # 将列表写成文本

# 案例：文件复制
# 操作系统的简单操作
import os
# os.rename("1.txt", "100.txt")  # 重命名
# os.remove("2.txt")  # 删除
# os.mkdir("new_filefold")  # 创建文件夹
print(os.path.exists("1.txt"))  # 判断文件是否存在

'''
格式化复制，复制后，name.txt变成name[复制].txt
'''
file_old_name = "Python.xlsx"
index = file_old_name.rfind(".")
file_new_name = file_old_name[:index] + "【复制】" + file_old_name[index:]
file_old = open(file_old_name, "rb")
file_new = open(file_new_name, "wb")
while True:
    info = file_old.read(1024)
    if len(info) != 0:
        file_new.write(info)
    else:
        break
file_old.close()
file_new.close()








