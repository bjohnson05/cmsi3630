###
# filename: bigOcompare.py
# purpose:  demonstration of where nlogn and n^2 cross
# author:   Dr. Johnson
# date:     2023-02-22
###

import sys
import math

def main():
   if( len( sys.argv ) < 2 ):
      print( "\n   You must enter an integer." )
      print( "   Please try again.\n" )
   else:
      data_size = float( sys.argv[1] )
      print( "\n\n   for data set of: ", data_size )
      print( "   Big-Oh( 8n log n)  is: ", (8 * data_size * math.log10( data_size )) )
      print( "   Big-Oh( 0.01 n^2 ) is: ", (0.01 * data_size * data_size ) )

main()
