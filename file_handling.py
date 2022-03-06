# #operation takes place in file handling
# # 1.open a file
# # 2.read or write 
# # 3.close the file

# f= open('data.txt', 'r') #path for data.txt  this will open in read and it will return file object
# # + mode can also be used for read & write

# # f.readline()  #first line will read
# # f.readline()  #2nd line will read

# #for print
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())

# for line in f:
#     print(line)

# f.close() 
# #but agar error ayi to file close nh hopati h that's why we use with


with open('data.txt') as f: #this will close automatically
    # for line in f:
    #  print(line)


 #this will read whole file
#  print(f.read())  

 #if u want to read some char only
print(f.read(10))  

f.seek(20)#this is used to move cursor
print(f.read(10)


