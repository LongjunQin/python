# 1.定义类
class Cat: # 类名要大驼峰规则：MyName
    pass
cat1 = Cat() # 创建对象

# 2.类成员：成员变量和成员方法
class Cat:
    def __init__(self): # 创建对象时自动运行，魔术方法
        '''
        成员变量共有属性
        '''
        self.type = "波斯猫"
        self.name = None
    
    def eat(self): # 成员方法
        print("猫吃鱼。")
    
    def climb(self, meter):
        print("猫爬树，爬了%d米。" % meter)
    
    def __str__(self): # 魔术方法，显示打印对象的信息
        return "猫对象。"
    
cat1 = Cat()
print(cat1.type) # 使用成员变量
cat1.cloth = 'red' # 成员变量独有属性，只有本对象可以使用
cat1.eat()
cat1.climb(10)
print(cat1)

# 3.成员方法调用成员变量和成员方法
class Cat:
    def __init__(self):
        self.type = "波斯猫"
        self.name = None
    
    def introduce(self):
        print("我是一只%s，我的名字是%s。" % (self.type, self.name)) # 调用成员属性
    
    def jump(self):
        print("猫跳起来。")

    def grasp(self):
        print("猫抓东西。")

    def bite(self):
        print("猫咬东西。")
    
    def catch(self):
        '''
        调用成员方法
        '''
        self.jump()
        self.grasp()
        self.bite()

cat = Cat()
cat.name = "Jack"
cat.introduce()
cat.catch()

'''
例：手机程序
手机初始电量是100
打游戏每次耗电10
听歌每次耗电5
打电话每次耗电4
接电话每次耗电3
充电给定的电量
'''
class Phone:
    def __init__(self):
        self.power = 100
    
    def game(self):
        print("打游戏耗电10.")
        self.power -= 10
    
    def music(self):
        print("听歌耗电5.")
        self.power -= 5
    
    def call(self):
        print("打电话耗电4.")
        self.power -= 4
    
    def answer(self):
        print("接电话耗电3.")
        self.power -= 3

    def charge(self, num):
        print("给手机充电%d." % num)
        self.power += num
    
    def __str__(self):
        return "目前手机电量是%d." % self.power
    
p = Phone()
p.game()
p.music()
p.call()
p.answer()
p.charge(10)
print(p)

'''
例：手机程序加强：
耗电程序前判断电量是否够
充电前确保不过冲
手机初始电量是100
打游戏每次耗电10
听歌每次耗电5
打电话每次耗电4
接电话每次耗电3
充电给定的电量
'''
class Phone:
    def __init__(self):
        self.power = 100
    
    def game(self):
        if self.power >= 10:
            print("打游戏耗电10.")
            self.power -= 10
        else:
            print("手机电量不足。")
    
    def music(self):
        if self.power >= 5:
            print("听歌耗电5.")
            self.power -= 5
        else:
            print("手机电量不足。")
    
    def call(self):
        if self.power >= 4:
            print("打电话耗电4.")
            self.power -= 4
        else:
            print("手机电量不足。")
    
    def answer(self):
        if self.power >= 3:
            print("接电话耗电3.")
            self.power -= 3
        else:
            print("手机电量不足。")

    def charge(self, num):
        if self.power + num <= 100:
            print("给手机充电%d." % num)
            self.power += num
        else:
            print("手机过冲，自动停止，电量是100.")
            self.power = 100
    
    def __str__(self):
        return "目前手机电量是%d." % self.power
    
p = Phone()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.game()
p.music()
p.call()
p.answer()
p.charge(111)
print(p)

# 4.封装：将属性设置为私有变量，通过get,set两个方法获取和修改。
class Card:
    def __init__(self):
        self.card_num = None 
        self.__card_pwd = None # 私有属性
    
    def get_pwd(self):
        return self.__card_pwd
    
    def set_pwd(self, pwd):
        self.__card_pwd = pwd

c = Card()
c.set_pwd(1234)
print(c.get_pwd())

# 5.__init__传参
class Cat:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    def __str__(self):
        return "猫的品种是%s, 猫的名字是%s。" % (self.type, self.name)

cat = Cat("波斯猫", "Jack")
print(cat)




