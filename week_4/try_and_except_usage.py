# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:29:08 2018

@author: Colton


try:#if this works, it will run it and skip "except"
    a = int(input("Tell me a number:"))
    b = int(input("Tell me another number:"))
    print(a/b)#answer is a float b/c there is only one forwardslash
    print(a//b)#answer is an int rounded down b/c there are two forwardslashes
    print("Okay")
except:#if something does not work, this will report a bug b/c of an excpetion raised in "try"
    print("Bug in user input.")
print("Outside")#execution continues (jump outside)



try:#if this works, it will run it and skip "except"
    a = int(input("Tell me a number:"))
    b = int(input("Tell me another number:"))
    print(a/b)#answer is a float b/c there is only one forwardslash
    print(a//b)#answer is an int rounded down b/c there are two forwardslashes
    print("Okay")
except ValueError:#allows us to decide which errors shall be excepted
    print("Could not convert to a number")
except ZeroDivisionError: #can't divide by zero
    print("Count not divide by zero")
except:#general other accept
    print("You messed up dude.")
break
print("Outside")#outside of try/except

'''
else:#happens after "try" if "try" has no exceptions
finally:#happens after EVERYTHING regardless of errors
'''

raise #raises exceptions when outcome is not what is wanted/preffered
raise _someerror_("insert message")
raise ValueError("number is wierd")#example
assert #this stops function immediately
assert (statement that is expected to be true), a string to print in response_ #asserts something that should be true/expected in your code
"""
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")