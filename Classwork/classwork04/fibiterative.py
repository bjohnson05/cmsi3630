###
# filename: fibiterative.py
# purpose:  demonstrate and iterative fibonacci sequence
# author:   Dr. Johnson
# date:     2023-01-26
###
import sys

def fibiterative( n ):
   print( "\n" )
   if( n == 0 or n == 1 ):
      print( "0" )
   elif( n == 2 ):
      print( "0  1" )
   else:
      print( "0  1  ", end="" )
      prev = 0
      current = 1
      for i in range(2, n):
         next = prev + current
         prev = current
         current = next
         print( next, " ", end="" )
   print( "\n" )

def main():
   if(len(sys.argv) == 1):
      raise ValueError("\n   You must enter one integer number!\n")
   else:
      fibiterative( int(sys.argv[1]) )

fibiterative( 0 )
fibiterative( 1 )
fibiterative( 2 )
fibiterative( 5 )
fibiterative( 10 )
fibiterative( 40 )

main()
