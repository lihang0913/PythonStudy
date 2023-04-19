#类的继承
class Partent:  # 定义父类
    parentAttr = 520

    def __init__(self):
        print('调用了父类构造函数')

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self,attr):
        Partent.parentAttr=attr

    def getAttr(self):
        print('父类属性 ：' ,Partent.parentAttr)

class Child(Partent): #定义子类
    def __init__(self):
        print('调用子类构造方法')

    def childMethod(self):
        print('调用子类方法')
a =Child()          # 实例化子类
a.childMethod()     # 调用子类的方法
a.parentMethod()    # 调用父类方法
a.setAttr(520)      # 再次调用父类的方法 - 设置属性值
a.getAttr()         # 再次调用父类的方法 - 获取属性值
