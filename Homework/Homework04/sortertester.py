###
# filename: sortertester.py
# purpose: tests for the odd/even sorter
# author:   Dr. Johnson
# date:     2023-03-27
###

from oddevensorter import oddEvenSort
from oddevensorter import display

print( "\n\n   WELCOME TO THE ODD-EVEN SORTER\n" )
a_list = [303, 202, 505, 101, 808, 707, 909, 404, 606, -222, -555, -789, -456, -123, 0]
print( "   Original list: ", end = "" )
display( a_list )
oddEvenSort( a_list )
print( "     Sorted list: ", end = "" )
display( a_list )
