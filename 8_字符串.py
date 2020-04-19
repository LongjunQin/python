# 1.字符串定义，字符串是容器
str1 = "Hello World。"  # 常用
str2 = 'hello world.'
str3 = '''hello world.lskdskldfja'''
str4 = """kdjal;fgjas;kld 
gjads;lkjgl;keqwjrgipoerwh
jgqpeioguer;""" # 可直接回车断行
s = "Hello \
World." # \ 转移字符断行
s = "hello world. \"he\" said."
print(s)

# 2.基本操作
str = "Hello World."
len(str)
max(str)
min(str)

# 3.判断 is
s = "Hello World."
print(s.islower())
print(s.isupper())
print(s.isprintable()) # /n, /t 就是不可打印
print(s.isdigit())
print('HelloWorld'.isalpha())
name = "Longjun Qin"
print(name.startswith("Long"))
filename = 'liu.jpg'
print(filename.endswith('.jpg'))

# 4.数据转换
s = "Hello World."
print(s.lower())
print(s.upper())
print(s.title())

# 5.格式转换
s = "*****Hello World****"
print(s.strip("*"))
print(s.lstrip("*"))
s = "Hello World."
print(s.ljust(20, "*")) # 一共占位20，如果字长大于占位，无变化，否则字左补右。
print(s.rjust(20, "*"))
print(s.center(20, "&")) # 一共占位20，不够的字中补&
print(s.zfill(20)) # 左侧补0

# 6.拆分连接
s = "Hello World."
print(s.partition("o")) # 拆成3块
print(s.rpartition("o"))
print(s.split('l')) # 去掉所有l,拆成列表
print(s.split('l', 2)) # 只切两次，一般不用
print(s.splitlines())
symbal = '_'
l = ['a', 'b', '3']
print(symbal.join(l)) # 用某个片段连接列表的元素，将其变成字符串
l = "hello "
l2 = "world"
print(l + l2)

# 7.查询替换
s = 'hello world.'
print(s.find('ll'))
print(s.rfind('l'))
print(s.find('1')) # 查询不到返回 -1，常用
print(s.index('l')) # 查询不到报错
print(s.replace("llo", "qin"))
print(s.replace("l", "love", 2)) # 只替换两个

# 8.加密解密
s = 'hello python'
d = "".maketrans('abcdefg', '1234567')
s_code = s.translate(d)
d2 = ''.maketrans("1234567", "abcdefg") # 解密
print(s_code.translate(d2))

'''
9.小结，常用的内容
len()
strip()
str[1:6]
str1 + str2
str[index]
'''

'''
10.案例，找嫌疑犯
张某
绰号：兵哥
男性
1975-1978年出生
B型血
河北口音
'''
infos = [] # 公安的人口数据库
for person in infos:
    name = person['name']
    nick_name = person['nick_name']
    gender = person['gender']
    id_card = person['id']
    blood = person['blood']
    native = person['native']
    # 如果有一项不匹配，就跳过查询下一项，全部匹配，打印信息
    if not name.startswith("张"):
        continue
    if name.find("兵") == -1 and nick_name.find("兵") == -1:
        continue
    if gender != 1:
        continue
    if int(id_card[6:10]) < 1975 or int(id_card[6:10]) > 1978:
        continue
    if blood.lower() != 'b':
        continue
    if native.find("河北") == -1:
        continue
    gender_dict = {1: "男性", 0: "女性"}
    print("name: %s, gender: %s" % (name, gender_dict[gender]))




