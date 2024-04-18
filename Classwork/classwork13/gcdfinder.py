###
# filename: gcdfinder.py
# purpose:  find the greatest common divisor
# author:   Dr. Johnson
# date:     2023-03-26
###

import sys

def gcd( a, b ):
   if( b == 0 ):
      return a
   else:
      return gcd( b, a % b )

def main():
   if( len( sys.argv ) != 3 ):
      print( "\n   Usage: python gcdfinder.py num1 num2\n\n" )
      num1 = int( input( "   Enter the first number: " ) )
      num2 = int( input( "   Enter the second number: " ) )
   else:
      print( "\n   GCD CALCULATOR\n" )
      num1 = int( sys.argv[1] )
      num2 = int( sys.argv[2] )
   print( "   The GCD of ", num1, " and ", num2, " is: ", gcd( num1, num2 ) )

main()

