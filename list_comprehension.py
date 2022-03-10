from ast import Expression


#syntax: new_list=[Expression           for items in list          if condition]

b=[x      for x in range(100)    if x%2==0]
print(b)

a=[    x           for x in range(10)]
# [expression     for items in list ]
print(a) #op [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

y=[3**i for i in range(10)]
print(y)

