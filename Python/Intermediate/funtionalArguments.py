'''
1) diff between parameter and argument
ans : parameters are num of variables used at time of defining function
arguments are variables passed into parameters
2)postional and keyword arguments and types ## keyword arguments follows positional arguments
3)default arguments
4)variable arguments *args, **kargs
'''


def fun1(a,b,c):
    print(a,b,c)

## postional arguments
fun1(1,2,3,)
##order matters

## key word arguments
print("\n")
fun1(a=1,b=2,c=3)
fun1(a=1,c=3,b=2)
print("\n")
## both yields same result, order doesn't matter in keyword arguments

## keyword and positional arguments are used toegther rule->(positional, keyword)
#fun1(a=1,2,3) -> throws a error
fun1(1,c=2,b=1) #-> works fine

'''variable length arguments'''
## to pass variable length arguments u need function with accepts variable length pf arguments
## *args as function parameter helps u collect variable length positional arguments (gets stored as tuple after collection)
## **kargs as function parameter helps u collect variable length key word arguments (gets stored as dictionary after collection)
## order -> *args,**kargs
print("\n")
def fun2(a,b,c,*args,**kargs):
    print(a,b,c)
    print("\n")
    for i in args:
        print(i,end=" ")
    print("\n")
    for i in kargs:
        print(kargs[i],end=" ")

fun2(1,2,3,4,5,6,seven=7,eight=8,nine=9)