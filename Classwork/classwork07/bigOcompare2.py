###
# filename: bigOcompare2.py
# purpose:  demonstration of where nlogn and n^2 cross
# author:   Dr. Johnson
# date:     2023-02-28
# Note:     Also uses numpy as a first example
###

import sys
import math
import numpy as np

def map1(x):
   return 8 * x * math.log10( x )

def map2(x):
   return 0.01 * x * x

def main():
   if( len( sys.argv ) < 3 ):
      print( "\n   You must enter two integers." )
      print( "   The first is the size of the array of values." )
      print( "   The second is the starting value of the array." )
      print( "   Please try again.\n" )
   else:
      data_size   = int( sys.argv[1] )
      start_value = int( sys.argv[2] )
      print( "\n\n   for data set of: ", data_size )
      print( "     and start value of: ", start_value )
      print()

      a = np.arange( data_size+1 )
      b = np.arange( data_size+1 )

      a *= data_size
      b *= data_size
      a += start_value
      b += start_value

      a = map( map1, a )
      b = map( map2, b )
      print( "a:", list(a) )
      print( "b:", list(b) )
      print()

      print( "   Big-Oh( 8n log n)  is: ", (8 * start_value * math.log10( start_value )) )
      print( "   Big-Oh( 0.01 n^2 ) is: ", (0.01 * start_value * start_value ) )

main()
