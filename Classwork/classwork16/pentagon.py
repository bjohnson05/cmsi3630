###
#  filename: pentagon.py
#  purpose: demonstration
#  author: Dr. Johnson
#  date: 2024-04-23
###

import math

def get_height( sideLength ):
   return (sideLength / 2) / math.tan( ((2 * math.pi) / 10 ))

def calculate( sideLength ):
   return ( sideLength * get_height( sideLength )) / 2

def main():
   length = float( input( "\n\n   enter the length of one side: " ) )
   print( "\n   Area of a regular pentagon of side length ", length )
   print( "     is: ", calculate( length ) * 5.0 )

main()
