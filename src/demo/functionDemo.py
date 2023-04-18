def sum(num1,num2):
	"两数之和"
	return num1+num2

def division (num1, num2):
	a = num1 % num2
	b = (num1-a) / num2
	return b,a

num1 , num2 =division(11, 5)
tuple1 = division(11,5)
print(num1,num2)
print(tuple1)

# 调用函数
# print(sum(5,6))

def print_user_info( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数

print_user_info( name = '水' ,age = 18 , sex = '女')
print_user_info( name = '水' ,sex = '女', age = 18 )


def print_user_info( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( '可苹' ,24 , '女', '撸管','看美女','打飞机')

def print_user_info1( name ,  age  , sex = '男' , ** hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info1( name = '陈可苹' , age = 24 , sex = '女', hobby = ('撸管','看美女','打飞机','变态男'))

print('----------------------')
def print_user_info2( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info2( name = '陈可苹' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
#print_user_info( '两点水' , 18 , '女' )
print_user_info2('陈可苹',age='22',sex='男')
print('----------------------')
sum = lambda num1 , num2 : num1 + num2;

print( sum( 1 , 2 ) )