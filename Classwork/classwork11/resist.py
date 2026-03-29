###
# filename: resist.py
# purpose: demonstrate resistance calculation
#           for parallel resistors
# author: Dr. Johnson
# date: 2026-03-28
#
# This program takes a list of resistance values from
#  the command line arguments and treats them as if they
#  are all in parallel with each other.  It calculates
#  the total resistance of the circuit and displays it.
###

import sys

def calculate():
   rList = []
   total = 0
   for i in sys.argv[1:]:
      rList.append( float( i ) )
   for i in rList:
      total += ( 1.0 / i )
   total = ( 1.0 / total )
   return total

def main():
   if( len( sys.argv ) == 1 ):
      print( "\n   Sorry you must enter at least one value.\n" )
   else:
      print( "\n   The total resistance is: ", calculate() )

main()
