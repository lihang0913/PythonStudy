#修改类的属性
class ClasA():
    var1="你好"
    @classmethod
    def fun1(cls):
        print("var1值为：" + cls.var1)

ClasA.fun1()
ClasA.var1 =  input("请输入修改的var1值：")
ClasA.fun1()
ClasA.var2 = input("请输入增加的var2值：")
print(ClasA.var2)