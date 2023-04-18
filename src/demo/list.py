#九九乘法表
# print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))
# gen= (x * x for x in range(10))
# for num  in  gen :
# 	print(num)
# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# # 引用函数
# for x in fibon(100):
#     print(x , end = ' ')
def triangles( n ):         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]

n= 0
for t in triangles( 10 ):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break