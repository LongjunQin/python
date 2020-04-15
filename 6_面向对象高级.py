# 1.类变量
class Cat:
    subject = "猫科动物" # 类变量

    def __init__(self, type, name): # 实例变量
        self.type = type
        self.name = name
# 类变量访问
c = Cat("波斯猫", "Jack")
print(Cat.subject) # 推荐
print(c.subject)
# 类变量修改
c2 = Cat("英国短毛猫", "Mary")
c.subject = "喵星人" # 声明本实例的新变量
print(c.subject)
print(Cat.subject)
Cat.subject = "喵喵" # 修改类变量
print(c2.subject)
print(Cat.subject)

# 2.类方法
class Chinese:
    nationality = "中国人"

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @classmethod
    def show_country(cls): 
        print("我是中国人")
# 类方法调用
c = Chinese("xiaoming", "235431t515")
Chinese.show_country() # 推荐
c.show_country()

# 3.类方法与实例方法的相互调用
class Chinese:
    nationality = "中国人"

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @classmethod # 类方法不能调用实例方法
    def show_country(cls): 
        print("我是中国人")
    
    def show(self):
        Chinese.show_country() # 实例方法可以调用类方法
        print("name: %s, id: %d" % (self.name, self.id))
c = Chinese("小名", 123416572642)
c.show()

# 4.静态方法
class Chinese:
    @staticmethod # 与对象无关的变量，可放在类外当函数
    def show():
        print("我是静态变量，在类里打酱油的。")

c = Chinese()
c.show()
Chinese.show()

'''
5.定义区分：
公有变量，局部变量（函数内的），私有变量，类变量，全局变量，独有变量。
成员变量 = 公有变量
对象属性 = 对象变量
实例方法，成员方法
类方法
静态方法
构造方法 __init__
对象 = 实例
'''
quanjubianliang = 1 # 全局变量
class Chinese:
    nationality = "中国人" # 类变量

    def __init__(self, name, id): # 共有变量：self.XXX
        self.name = name
        self.id = id
        self.__secret = None # 私有变量
    
    @classmethod
    def show_country(cls): 
        print("我是中国人")
    
    @staticmethod # 与对象无关的变量，可放在类外当函数
    def show():
        print("我是静态变量，在类里打酱油的。")
c = Chinese("小名", 1451513)
c.cloth = "red" # 独有变量
print(c.cloth)

'''
6.继承
类间关系
子类获取父类信息
子类可有父类没有的属性与方法
父类私有属性子类无法继承
'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__secret = None # 父类私有属性子类无法继承
    
    def show(self):
        print("我是一只小动物，名字是: %s" % self.name)

class Cat(Animal):
    def climb(self): # 子类独有方法
        print("猫会爬树。")

c = Cat("Jack", 2)
c.show()

'''
7.类的关系结构图
'''
class Animal:
    pass

class Cat(Animal):
    pass

class PersianCat(Cat):
    pass

print(PersianCat.__mro__)
# <class '__main__.PersianCat'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>
print(Cat.__mro__)

'''
8.重写:继承时，子类与父类重名的方法，子类调用重写方法，执行子类的方法。
'''
class Animal:
    def eat(self):
        print("动物吃东西。")

class Cat(Animal):
    def eat(self):
        print("猫吃鱼。")
    
    def __str__(self): # 重写方法
        return "喵星人"

cat1 = Cat()
cat1.eat()

'''
9.重写后调用被子类覆盖的方法
'''
class Animal:
    def __init__(self):
        print("动物被创建")


    def eat(self):
        print("动物吃东西。")

class Cat(Animal):
    def __init__(self):
        print("猫被创建")
        print("----------")
        Animal.__init__(self)
        super(Cat, self).__init__()
        super().__init__() # 推荐


    def eat(self):
        print("猫吃鱼。")
        Animal.eat(self) # 方法一
        super(Cat, self).eat() # 方法二
        super().eat() # 方法三 推荐

    
    def __str__(self): 
        print("-----------------")
        temp = Animal.__str__(self)
        print(temp)
        temp = super(Cat, self).__str__()
        print(temp)
        temp = super().__str__()  # 推荐
        print(temp)
        print("-----------------")
        return "喵星人"

cat1 = Cat()
cat1.eat()
print(cat1)

'''
10.多继承
方法冲突，谁在前调谁
一定要同时调可以参考调用父类的方法
'''
class Father:
    def sing(self):
        print("爸爸会唱歌。")
    
    def dance(self):
        print("爸爸不会跳舞。")

class Mother:
    def sing(self):
        print("妈妈不会唱歌。")

    def dance(self):
        print("妈妈会跳舞。")

class Child(Father, Mother):
    def sing(self):
        print("儿子继承父母的唱歌天赋。")
        Father.sing(self)
        Mother.sing(self)
        super().sing() # 调用近的
c = Child()
c.sing()
print(Child.__mro__) # 查看继承结构

'''
11.多态：在不同环境展现不同的特征与功能
'''
class Teacher:
    def teach(self):
        print("教学生上课。")

class Driver:
    def drive(self):
        print("会开车。")

class Man(Teacher, Driver):
    pass

class Dome:
    def play(self, driver):
        driver.drive()

d = Dome()
man = Man()
d.play(man) # man继承了多个父类，在不同环境中展现不同父类的特征。

'''
12.鸭子类型
特殊的多态
语法层面满足调用关系，实际不具有对应的对象形态
'''
class Teacher:
    def teach(self):
        print("教你python。")

class Man(Teacher):
    pass

class GamePlayer:
    def teach(self):
        print("教你打游戏。")

class Demo:
    def learn(self, teacher):
        teacher.teach()

man = Man()
player = GamePlayer()
d = Demo()
d.learn(man)
d.learn(player) # 鸭子形态

'''
13.引用类型参数：对象作为参数传入函数，函数对其属性进行改变，原对象属性跟着变
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name1 = "小王"
age1 = 18
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
p1 = Person("小赵", 30) # p1是内存存储空间

def demo(name, age, person):
    name = "改变你"
    age = 20
    person.name = "变名字"
    person.age = 21

print(name1)
print(age1)
print(p1.name)
print(p1.age)
print("----------------")
demo(name1, age1, p1)
print(name1)
print(age1)
print(p1.name)
print(p1.age)

'''
14.反恐精英案例
一个反恐精英打三个恐怖分子
初始生命值都是100
枪战一方生命值0结束
状态：100，无伤；70-90，轻伤；1-69，重伤；0，死亡
'''
class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100
    
    def __str__(self):
        return "%s的生命值是%d" % (self.name, self.life)

class Hero(Person):
    def fire(self, p):
        damage = 40
        print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
        p.life -= damage


class Is(Person):
    def fire(self, p):
        damage = 10
        print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
        p.life -= damage



def main():
    h = Hero("【英雄】")
    is1 = Is("【恐怖分子一号】")
    while True:
        h.fire(is1)
        is1.fire(h)
        print(h)
        print(is1)
        if h.life <= 0:
            print("英雄死亡，游戏结束。")
            break
        if is1.life <= 0:
            print("恐怖分子全部死亡，游戏结束。")
            break


main()

'''
15.反恐精英案例修正
每轮分开
重写Hero声明显示状态：100，无伤；70-90，轻伤；1-69，重伤；0，死亡
修改生命值为负值
'''
class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100
    
    def __str__(self):
        return "%s的生命值是%d" % (self.name, self.life)

class Hero(Person):
    def fire(self, p):
        damage = 40
        if p.life > 40:
            print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
            p.life -= damage
        else:
            print("%s挂了，血量为0" % (p.name))
            p.life = 0

    def __str__(self): # 展示英雄状态
        if self.life == 100:
            return "【英雄】无伤"
        elif self.life > 70 and self.life < 100:
            return "【英雄】轻伤"
        elif self.life > 1 and self.life < 70:
            return "【英雄】重伤"
        else:
            return "【英雄】挂了"

class Is(Person):
    def fire(self, p):
        damage = 80
        if self.life < 0:
            print("%s向%s开枪，%s生命值为0。" % (self.name, p.name, p.name))
            self.life = 0
        else:
            print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
            p.life -= damage

def main():
    h = Hero("【英雄】")
    is1 = Is("【恐怖分子一号】")
    while True:
        h.fire(is1)
        is1.fire(h)
        print(h)
        print(is1)
        print("=====================================") # 每轮隔开
        if h.life <= 0:
            print("英雄死亡，游戏结束。")
            break
        if is1.life <= 0:
            print("恐怖分子全部死亡，游戏结束。")
            break
main()

'''
16.反恐精英案例加强版
打三个恐怖分子
'''
import random

class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100
    
    def __str__(self):
        return "%s的生命值是%d" % (self.name, self.life)

class Hero(Person):
    def fire(self, p):
        damage = 40
        if p.life > damage:
            print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
            p.life -= damage
        else:
            print("%s挂了，血量为0" % (p.name))
            p.life = 0


    def __str__(self): # 展示英雄状态
        if self.life == 100:
            return "【英雄】无伤"
        elif self.life > 70 and self.life < 100:
            return "【英雄】轻伤"
        elif self.life > 1 and self.life < 70:
            return "【英雄】重伤"
        else:
            return "【英雄】挂了"

class Is(Person):
    def fire(self, p):
        damage = 1
        if self.life < 0:
            print("%s向%s开枪，%s生命值为0。" % (self.name, p.name, p.name))
            self.life = 0
        else:
            print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
            p.life -= damage

def main():
    h = Hero("【英雄】")
    is1 = Is("【恐怖分子一号】") # 创建三个恐怖分子
    is2 = Is("【恐怖分子二号】")
    is3 = Is("【恐怖分子三号】")
    while True:
        x = random.randint(1, 3) # 英雄挑一个恐怖分子打
        if x == 1:
            h.fire(is1)
        elif x == 2:
            h.fire(is2)
        else:
            h.fire(is3)
        is1.fire(h) # 三个恐怖分子都开枪
        is2.fire(h)
        is3.fire(h)
        print(h)
        print(is1) # 三个恐怖分子都显示状态
        print(is2)
        print(is3)
        print("=====================================") # 每轮隔开
        if h.life <= 0:
            print("英雄死亡，游戏结束。")
            break
        if is1.life <= 0 and is2.life <= 0 and is3.life <= 0: # 三个恐怖分子都死亡，游戏结束
            print("恐怖分子全部死亡，游戏结束。")
            break
main()

'''
17.反恐精英案例加强版
加入开枪命中率，80%，20%
加入伤害波动，20-50，5-15
鞭尸
'''
import random

class Person:
    def __init__(self, name):
        self.name = name
        self.life = 100
    
    def __str__(self):
        return "%s的生命值是%d" % (self.name, self.life)

class Hero(Person):
    def fire(self, p):
        hit = random.randint(1, 100)
        if hit >= 20:
            damage = random.randint(20, 50)
            if p.life > 0:
                if p.life > damage:
                    print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
                    p.life -= damage
                else:
                    print("%s挂了，血量为0" % (p.name))
                    p.life = 0
            else:
                print("%s已经挂了，去打别的恐怖分子啊。" % p.name)
        else:
            print("%s没打中%s." % (self.name, p.name))

    def __str__(self): # 展示英雄状态
        if self.life == 100:
            return "【英雄】无伤"
        elif self.life > 70 and self.life < 100:
            return "【英雄】轻伤"
        elif self.life > 1 and self.life < 70:
            return "【英雄】重伤"
        else:
            return "【英雄】挂了"

class Is(Person):
    def fire(self, p):
        hit = random.randint(1, 100)
        if hit >= 80:
            damage = random.randint(5, 15)
            if self.life < 0:
                print("%s向%s开枪，%s生命值为0。" % (self.name, p.name, p.name))
                self.life = 0
            else:
                print("%s向%s开枪，造成%s的%d生命值伤害。" % (self.name, p.name, p.name, damage))
                p.life -= damage
        else:
            print("%s没有打中%s." % (self.name, p.name))

def main():
    h = Hero("【英雄】")
    is1 = Is("【恐怖分子一号】") # 创建三个恐怖分子
    is2 = Is("【恐怖分子二号】")
    is3 = Is("【恐怖分子三号】")
    while True:
        x = random.randint(1, 3) # 英雄挑一个恐怖分子打
        if x == 1:
            h.fire(is1)
        elif x == 2:
            h.fire(is2)
        else:
            h.fire(is3)
        if is1.life > 0:
            is1.fire(h) # 三个恐怖分子都开枪
        if is2.life > 0:
            is2.fire(h)
        if is3.life > 0:
            is3.fire(h)
        print(h)
        print(is1) # 三个恐怖分子都显示状态
        print(is2)
        print(is3)
        print("=====================================") # 每轮隔开
        if h.life <= 0:
            print("英雄死亡，游戏结束。")
            break
        if is1.life <= 0 and is2.life <= 0 and is3.life <= 0: # 三个恐怖分子都死亡，游戏结束
            print("恐怖分子全部死亡，游戏结束。")
            break
main()

    






