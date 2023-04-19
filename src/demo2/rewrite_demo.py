#类的重写
class Parent:
    def myMethood(self):
        print('调用父类方法')
class Child(Parent):
    def myMethood(self):
        print('调用子类方法')

a = Child() # 子类实例
a.myMethood() #子类调用重写方法