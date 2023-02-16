###
# filename: Die.py
# purpose:  Dice game class example
# author:   Dr. Johnson
# date:     2023-01-06
###

import random
import math

class Die:
   sides = 4      # default for minimum number of sides
   value = 0      # default starting value

   def __init__( self, numberOfSides ):
      if( numberOfSides < 4 ):
         raise IllegalArgumentException( " must have at least 4 sides." )
      else:
         self.sides = numberOfSides

   def roll( self ):
      self.value = random.randint( 0, self.sides )
      return self.value

   def getValue( self ):
      return self.value

   def toString( self ):
      rep = "[{}]".format( self.value )
      return rep

def main():
   d1 = Die( 4 )
   print( "\n   Die 1 created ~ sides: ", d1.sides )
   print( "\n   Die 1 created ~ value: ", d1.value )
   d1.roll()
   print( "\n   Die 1 rolled  ~ value: ", d1.value )
   print( "   Die 1 rolled  ~ value: ", d1.roll() )
   print( "   Die 1 rolled  ~ value: ", d1.roll() )
   print( "   Die 1 rolled  ~ value: ", d1.roll() )
   print( "   Die 1 rolled  ~ value: ", d1.roll() )
   print( "   Die 1 rolled  ~ value: ", d1.roll() )
   print( "   Die 1 getValue() says: ", d1.getValue() )
   print( "   Die 1 representation : ", d1.toString() )
   d2 = Die( 17 );
   print( "\n   Die 2 created ~ sides: ", d2.sides )
   print( "\n   Die 2 created ~ value: ", d2.value )
   d2.roll()
   print( "\n   Die 1 rolled  ~ value: ", d1.value )
   print( "   Die 2 rolled  ~ value: ", d2.roll() )
   print( "   Die 2 rolled  ~ value: ", d2.roll() )
   print( "   Die 2 rolled  ~ value: ", d2.roll() )
   print( "   Die 2 rolled  ~ value: ", d2.roll() )
   print( "   Die 2 rolled  ~ value: ", d2.roll() )
   print( "   Die 2 getValue() says: ", d2.getValue() )
   print( "   Die 2 representation : ", d2.toString() )
   print( "\n   Die 1 value: ", d1.value )
   print( "\n   Die 2 value: ", d2.value )
   print( "   Die 1 getValue() says: ", d1.getValue() )
   print( "   Die 1 representation : ", d1.toString() )

# main()
