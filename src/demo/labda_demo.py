# squareA=lambda a : a * a
# print(squareA(5))

mapA = map(lambda x : ord(x) + 10,"FishC")

print(list(mapA))

def boring(a):
    return ord(a)+10
boringA=list(map(boring,"FishC"))
print(boringA)

listA=list(filter(lambda b :b % 2,range(10)))
print(listA)

