# dict1={'one':'111111' ,'two':'222222' ,'两点水':'333333'}
dict2={'abc':1234,1234:'abc'}
# print(dict1)
# print(dict2)
# print(dict1['one'])
# print(dict2['abc'])
dict1={'one':'111111' ,'two':'222222' ,'两点水':'333333'}
print(dict1)
# 通过 key 值，删除对应的元素
del dict1['two']
print(dict1)
# 删除字典中的所有元素
dict1.clear()
print(dict1)
# 删除字典
# del dict1
print("dict1=========")
print(dict2)
print(len(dict2))
print(str(dict2))
print(dict2.values())
print(dict2.items())