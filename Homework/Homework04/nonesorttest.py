### 
# filename: nonesorttest.py.py 
# purpose: check out where 'None' goes when sorting
# author:   Dr. Johnson 
# date:     2023-04-28
### 

def sortNone():
   myList = [ None, 'a', 'z', 'c', 'd' ]
   print( "\n\n   original list: ", myList )
   print( "   sorted list: ", myList.sort() )

sortNone()
