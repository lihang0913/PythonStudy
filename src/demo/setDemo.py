# set1=set([123,456,789])
# print(set1)
# # set1.add(100)
# print(set1)
# # set1.add(100)
# print(set1)
# set1.remove(123)
# print(set1)



i = 2
while(i < 50):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : 
    print (i, " 是素数")
   i = i + 1
 
print ("Good bye!")