class ClassA(object):
    var1 = "test"
    def fun1(self):
        print("var1的值为："+self.var1)
#实例化
a=ClassA()
#实例化之后，使用类中的方法
a.fun1()
#使用属性
# print(a.var1)

def newFun(self):
    print("你好，我们可以做朋友吗？")

a.fun1=newFun
a.fun1()



