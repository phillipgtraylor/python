"""For the learners: you should know that doing something like the setup for 
this challenge inclines you to do is a bad practice. Never do the following:"""

# def f():
# 	if condition:
#    	return True
#    else:
#    	return False
"""This is just dumb. You are returning a boolean, so why even use if blocks in 
the first place? The correct what of doing this would be:"""


def f():
    return condition


"""Because this already evaluates as a boolean.

So in this challenge, forget about ifs and elses,
 and that leap variable, and just do the following:"""


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


"""code below is my submission. above is interesting if working with booleans though"""


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


year = int(raw_input())
