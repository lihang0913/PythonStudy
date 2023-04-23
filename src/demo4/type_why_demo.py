# 整形
age = 23
# print(age.__class__)
# 字符串
name = '你好，时间'
# print(name.__class__)

# 函数
def fu():
    pass

# print(fu.__class__)

# 实例
class eat(object):
    pass

myEat = eat()
# print(myEat.__class__)

print(age.__class__.__class__)
print(name.__class__.__class__)
print(fu.__class__.__class__)
print(myEat.__class__.__class__)