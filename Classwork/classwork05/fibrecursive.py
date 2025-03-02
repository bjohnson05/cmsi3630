###
# filename: fibrecursive.py
# purpose:  demonstrate a recursive fibonacci algorithm
# author:   Dr. Johnson
# date:     2023-01-26
###

def fibrecursive( n ):
   if( n <= 1 ):
      return n
   else:
      return( fibrecursive( n - 1 ) + fibrecursive( n - 2 ) )

for i in range( 20 ):
   print( fibrecursive(i), " ", end="" )
