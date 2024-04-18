###
# filename: swaptest.py
# purpose: demo of swapping/returning two things
# author:   Dr. Johnson
# date:     2023-04-14
###

def swapTest( value1, value2 ):
   temp = value1
   value1 = value2
   value2 = temp
   return value1, value2

num1 = ['A', 23]
num2 = ['B', 17]
print( "num1: ", num1, " and num2: ", num2 )
num1, num2 = swapTest( num1, num2 )
print( "num1: ", num1, " and num2: ", num2 )
