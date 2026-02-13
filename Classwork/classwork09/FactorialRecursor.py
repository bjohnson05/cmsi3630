### 
# filename: FactorialRecursor.py 
# purpose:  demonstrate recursion
# author:   Dr. Johnson 
# date:     2023-02-20
### 

import sys

def factorial( n ):
#   print( "   N is: ", n )
   if( n <= 0 ):
      return 1
   else:
      return( n * factorial( n - 1 ) )

def main():
   if len(sys.argv) == 1:
      count = int( input( "\n   Enter an integer number: " ) )
   else:
      count = int( sys.argv[1] )
   print( "\n   The value of ", count, " factorial is: ", factorial( count ) )

main()
