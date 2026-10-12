from enum import Enum

## its used to keep values contant

class State(Enum):  ## State is the enum here
    active = 1
    inactive = 0

print(State.active)
print(State.active.value, "now we can asscess value of active")
print(list(State)) ## to see list variable in 'state' enum
print(len(State))

print("\n\n")

## updation using func
integer = 2
string ="abcd"

def change_immutable(integer, string):
    integer = 1
    string = "xyz"

change_immutable(integer,string)

print(integer)
print(string)

## u can't update immutables data types using function bc they create their own local copy of variable with updated values

## but can update mutable data types using functions

dictionary = {"a":1, "b":2, "c":3}

def change_mutable(dictionary):
    dictionary["a"]=45

print(dictionary["a"])
change_mutable(dictionary)
print(dictionary["a"])

'''
objects
everything is a object in python
int 
string
list 
dictionary
when u try update a immutable object for example int, count = 0 -> count = count+1 
here python will create whole new object its not old the object 
but 
when try u update something in mutable datatype 
the values in same object in gets updated
'''

'''
break - stop runnning loop entirely
continue - will just skip current iteration 
'''

