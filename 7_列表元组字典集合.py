# 1.列表
list1 = [1, 2, 3, 'itcast', True, None]
print(list1)
print(list1[0])
list1[4] = 'coder'
for i in list1:
    print(i)

'''
2.元组:元素不允许改
用处是自动组包和解包，打印字符串
'''
tuple1 = (1, 2, 3, 'itcast', True)
print(tuple1)
tuple2 = (2,) # 单个元组数据，需要加逗号。
print(tuple1[4])
for data in tuple1:
    print(data)

class Man:
    def __init__(self, name):
        self.name = name
man = Man("Jack")
t = (man,) 
man.name = "Mary" # 引用变量，内存不变，但是其属性可以变。
print(t)

def test():
    return 1, 2 # 自动组包
a, b = test() # 自动解包
print("a: %d, b: %d" % (a, b)) # 格式化打印

# 3.集合，无序，不重复
set1 = {1, 2, 3}
print(set1)
for data in set1:
    print(data)
set2 = {1, 2, 3, 5, 3, 2, 1}
print(set2)
set3 = {True, 1}
print(set3)
set3 = {2, True, 1}
print(set3)
set3 = {0, False}
print(set3)

# 4.三者互转
l = [1, 2, 3, 2, 1]
t = (1, 2, 3)
s = {1, 2}
print(tuple(l))
print(set(l))

# 5.字典：键值对key:value
dict1 = {'aa': "aa1", 'bb': 'bb2'}
dict1['aa'] = "膝盖"
print(dict1)
for key in dict1: # 取键
    print(key)
# 代替对象展示属性
class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dict2 = {'name': 'Jack', "age": 13}

# 6.range
n = range(5) # 不包括5
print(n)
print(list(range(10)))
print(list(range(2, 20, 3))) # 开始（包括），终止（不包括），步长
# range做循环
for _ in range(6): # _ 循环变量，无意义。
    print(_)

# 7.常用方法
list1 = [1, 3, 2]
list1.append(10)
print(list1)
print(list1.__len__()) # 查看长度
print(len(list1))
list1.sort() # 排序
print(list1)
list1.sort(reverse = True) # 排序反转
print(list1)
list1.insert(2, 'itcast') # 插入
print(list1)
l1 = [1, 2]
l2 = [3, 4]
t1 = (1, 2, 3)
l1.extend(l2) # 合并列表
print(l1)
l1.extend(t1) # 元组和列表可以合并一起
print(l1)
print(l1.index(3)) # 根据索引查元素
print(l1.count(1)) # 查询某个元素的个数
set1 = {1, 2, 3, 4, 5}
set1.add(6) # 集合的添加方法
print(set1)
dict1 = {"name": 'Jack', 'age': 18}
dict1['height'] = 1.76 # 添加 or 修改
print(dict1)
dict1['name'] # 查询1
dict1.get("name") # 查询2，推荐，查不到返回None,不报错。
print(dict1.keys()) # 取键
print(dict1.values()) # 取值
print(dict1.items()) # 元组形式取键值对

# 8.列表嵌套
l = [1, 2, 3]
s = {4, 5, 6}
t = (7, 8, 9)
list1 = [l, s, t, 100]
print(list1)
for element in list1:
    if isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
        for data in element:
            print(data)
    else:
        print(element)

'''
9.打牌游戏，不加大小王52，大小王2张
有一个牌堆，54张
三个玩家，没人17张，
留三个地主牌
初始化牌
洗牌
发牌
'''

import random
class Card:
    cards = []
    player1 = []
    player2 = []
    player3 = []
    last = []

    def __init__(self, flower, num):
        self.flower = flower
        self.num = num 

    @classmethod
    def init_cards(cls):
        flowers = ("♠", "♥", "♣", "♦")
        nums = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        for flower in flowers:
            for num in nums:
                cls.cards.append(Card(flower, num)) # 添加牌对象
        cls.cards.append(Card("大王", "")) # 大王，小王
        cls.cards.append(Card("小王", ""))

    @classmethod
    def wash_cards(cls):
        for idx in range(54):
            idxx = random.randint(0, 53)
            cls.cards[idx], cls.cards[idxx] = cls.cards[idxx], cls.cards[idx] # 互换 a, b = b, a
        

    @classmethod
    def send_cards(cls):
        for _ in range(17):
            cls.player1.append(cls.cards.pop(0))
            cls.player2.append(cls.cards.pop(0))
            cls.player3.append(cls.cards.pop(0))
        cls.last = cls.cards

    @classmethod
    def show_player_cards(cls):
        print("玩家一：", end = '')
        for card in cls.player1:
            print(card, end = ' ')
        print()
        print("玩家二：", end = '')
        for card in cls.player2:
            print(card, end = ' ')
        print()
        print("玩家三：", end = '')
        for card in cls.player3:
            print(card, end = ' ')
        print()
        print("地主牌：", end='')
        for card in cls.last:
            print(card, end=' ')
        print()

    # @classmethod # 打印牌
    # def show(cls):
    #     for card in cls.cards:
    #         print(card, end = ' ')


    def __str__(self):
        return "%s%s" % (self.flower, self.num)

Card.init_cards()
Card.wash_cards()
Card.send_cards()
Card.show_player_cards()

# 10.公共语法
# 容器
l = [1, 2, 3]
print(len(l))
print(max(l))
print(min(l))

# 切片
t = (1, 2, 3, 4, 5, 6)
print(t[2:4]) # 左包右不包
print(t[1:4:2]) # 第三个是步长
print(t[::-1]) # 步长为负，倒序打印

# 通用运算
l1 = [1, 2, 3]
l2 = [4, 5, 6]
t1 = (10, 11)
l1 = l1 + l2
print(l1)
l1 = l1 * 2
print(l1)
print(2 in l1)
print(20 in l1)
print([1, 2] < [2, 4])

# for...else... 如果for能执行完，就执行else
for _ in range(10):
    print(_)
else:
    print("end.")

for _ in range(10):
    print(_)
    if _ == 4:
        break
else:
    print("end.")

# 推导式
l1 = [i**2 for i in range(1, 100) if i % 2 == 0 and i % 7 == 0]
print(l1)
d = {'k1': 'v1', 'k2': 'v2'}
d2 = {d[key]: key for key in d} # 字典键值互换
print(d2)








