###
# filename: Square.py
# purpose: demonstration of subclassing
# author:   Dr. Johnson
# date:     2024-04-16
###

import math

# Define a Square subclass from Polygon
#  Overrides the 'area()' from the superclass
class Square( Polygon ):
   def __init__( self, side ):
      super().__init__( 4 )
      self.sideLength = side

   def area( self ):
      return self.sideLength ** 2

