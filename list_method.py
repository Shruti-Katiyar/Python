#append



a=[1,2,3]
a.append(4) #this will add 4 at last
a[1]=19

print(a)


#insert
b=[1 ,2,3,4]
b.insert(1,50) #1st idx per 50 insert hogha
print(b)


#sort

fruits=['banana','apple','kiwi']
fruits.sort()
print(fruits)

c=[4,3,2,1]
c.sort()
print(c)

#pop
c.pop(0) #0th idx will pop
print(c)

c.clear() #empty kr daygha
print(c)

fruits.reverse()
print(fruits)

print(fruits.index('apple')) #this will give idx of apple

print(fruits.count('kiwi')) #freq of element



