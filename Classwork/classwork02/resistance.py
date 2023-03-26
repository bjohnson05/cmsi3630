### 
# filename: resistance.py 
# purpose:  calculate parallel resistance
# author:   Dr. Johnson 
# date:     2023-01-16
### 

import sys

def resistance( values ):
   sum = 0
   for x in values:
      sum += ( 1.0 / float( x ) )
   total = 1 / sum
   print( f"\n Total parallel resistance is: {total:7.5} ohms")

def main():
   print( "\n  Calculating parallel resistance for values:", end=" " )
   for i in range( 1, len( sys.argv ) ):
      print( sys.argv[i], end=" " )
   print()
   n = len( sys.argv )
   newlist = sys.argv.copy()
   newlist.pop(0)
   resistance( newlist )

main()
