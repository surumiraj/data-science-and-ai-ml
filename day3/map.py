values=[1,2,3,4,5,6,7,8,9]
a=list(map(lambda x:x+2,values))
print(a)

b=list(filter(lambda x:x%2==0,values))
print(b)

from functools import reduce
c=reduce(lambda x,y:x+y,values)
print(c)
