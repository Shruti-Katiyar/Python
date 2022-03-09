
# we can generate sequence of no using range function

# a=range(10)

# print(a) 
#  #o/p will be range(0,10) it will not generate no it will only give range


# TO GENERATE NO WE USE LIST and we can pass 3 arrugument in range


#if we pass only 1 arrugument then it denote range kha per finish ho rhi h and start 0 say hota h by dafault
a=list(range(10))

print(a) 
#o/p will ne [0,1,2,3,4,5,6,7,8,9]

#if pass 2 arr the 1st  will be inclusive & 2nd will be exclusive
b=list(range(5,10))
print(b)
#o/p : [5,6,7,8,9]

#if pass 3 this means kya kya step lainy h
c=list(range(5,11,2))
print(c)
#op:[5,7,9]






