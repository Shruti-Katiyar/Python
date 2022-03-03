#key value pair store kr sktai h
#use {}

# marks={'rashi':34 , 'anuj': 12 , 'ram':25}

# marks={'rashi':34 , 'anuj': 12 , 'ram':25, 33:56 , 88:99}
# # print(marks['rashi']) #o/p 34  key find kr rha 
# print(marks['ram'])
# print(marks[33])  

                                      #iteration in dictionary

# solve={1:1 , 3:4  , 5:55}
# for i in solve:
#     print(solve[i]) #only key will op

                                       #updating dictionary items

marks={'rashi':34 , 'anuj': 12 , 'ram':25, 33:56 , 88:99}
marks['rohit']=55

print(marks) #tis will insert rohit in last

marks['anuj']=40
print(marks)#this will update marks of anuj

