###
#  filename: resist.py
#  calculate total parallel resistance
###

import sys

def calc( input ):
   total = 0
   for x in input[1:]:
      print( "  in loop, x: ", x, end=" " )
      total += 1.0 / float( x )
      print( "and total: ", total )
   return 1.0 / total

print( "\n   Total resistance is: ", calc( sys.argv ) )
