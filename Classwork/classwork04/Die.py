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

   def __init__( self, number_of_sides ):
      if( number_of_sides < 4 ):
         raise IllegalArgumentException( " must have at least 4 sides." )
      else:
         self.sides = number_of_sides

   def roll( self ):
      self.value = random.randint( 1, self.sides )
      return self.value

   def get_value( self ):
      return self.value

   def toString( self ):
      rep = "[{}]".format( self.value )
      return rep


###
# This section is to test the above code...
#  comment it out using the three-tic comment thing
#  uncomment it if you want to run it, otherwise
#  use the code in 'DiceSet.py' to run tests
###
'''
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
print( "   Die 1 get_value() says: ", d1.get_value() )
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
print( "   Die 2 get_value() says: ", d2.get_value() )
print( "   Die 2 representation : ", d2.toString() )
print( "\n   Die 1 value: ", d1.value )
print( "\n   Die 2 value: ", d2.value )
print( "   Die 1 get_value() says: ", d1.get_value() )
print( "   Die 1 representation : ", d1.toString() )
'''
