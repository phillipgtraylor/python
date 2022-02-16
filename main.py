# SPDX-License-Identifier: MIT

"""
Write a python program that iterates the integers from 1 to 50. 
For multiples of three print "Cloud" instead of the number
For multiples of seven print "Computing"
For numbers which are multiples of both three and seven print "CloudComputing"
"""
cloud3computing7 = []
var = 1
while var < 51:
    if var % 3 == 0 and var % 7 == 0:
        cloud3computing7.append("CloudComputing")
    elif var % 3 == 0:
        cloud3computing7.append("Cloud")
    elif var % 7 == 0:
        cloud3computing7.append("Computing")
    #    code below adds the non multiples of 3 and 7 or 3 or 7
    #    elif var == var:
    #        cloud3computing7.append(var)
    var = var + 1
print(cloud3computing7)
