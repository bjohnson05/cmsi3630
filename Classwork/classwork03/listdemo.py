###
# filename: listdemo.py
# purpose:  basic list demo
# author:   Dr. Johnson
# date:     2023-01-05
###

myList = list()
my_list = []
myList2 = [2, 3, 5, 7, 11, 13, 17, 19, 23 ]
myList3 = [29, 31, 37, 41, 47, 53]
myList4 = myList2
myList4.extend( myList3 )
count = 53
print( "\n  myList : ", myList  )
print( "\n  my_list : ", my_list  )
print( "\n  myList2: ", myList2 )
print( "\n  myList3: ", myList3 )
print( "\n  myList4: ", myList4 )
print( "\n  myList2[3]: ", myList2[3] )
print( "\n  myList2[-1]: ", myList2[-1] )
print( "\n  length of myList4: ", len( myList4 ) )
print( "\n  range of values 2:5 is: ", myList4[2:5] )
