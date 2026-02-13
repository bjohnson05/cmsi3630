'''
filename: fizzbuzz.py
purpose: demonstrator
author: Dr. Johnson
Date: 2025-02-20
Description: Play the game of 'fizz-buzz' in which you
   print the count from 1 to a number, except if the
   number is a factor of three you print 'fizz' and if
   it is a factor of five you print 'buzz'.  If it is
   a factor of BOTH, you print 'fizzbuzz'.
'''

def fizzbuzz( n ):
   if( ((n % 3) == 0) and ((n % 5) == 0)):
      print( "fizzbuzz" )
   elif( (n % 3) == 0 ):
      print( "fizz" )
   elif( (n % 5) == 0 ):
      print( "buzz" )
   else:
      print( n )

def main():
   print( "\n\n   Welcome to fizzbuzz!\n" )
   max = int( input( "   Enter the max number: " ) )
   for i in range( 1, max + 1 ):
      fizzbuzz( i )


main()