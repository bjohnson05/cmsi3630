'''
filename: fizzbuzz.py
purpose: demonstrator
author: Dr. Johnson
date: 2025-02-20
'''

def fizzbuzz( number ):
   if( ((number % 3) == 0) and ((number % 5) == 0) ):
      print( "fizzbuzz" )
   elif( (number % 3) == 0 ):
      print( "fizz" )
   elif( (number % 5) == 0 ):
      print( "buzz" )
   else:
      print( number )
   
def main():
   max = int( input( "\n\n   Enter a number less than 25: " ) )
   for i in range( 1, max + 1 ):
      fizzbuzz( i )

main()