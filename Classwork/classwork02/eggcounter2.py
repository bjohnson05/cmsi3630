"""
 An application that prompts the user for a number of eggs, and reports this
 number in grosses and dozens.
"""

import math

ONE_GROSS = 144
ONE_DOZEN = 12
MAX_COUNT = 1000000000
GREAT_GROSS = ONE_GROSS * 12

def instructions():
   print( "\n Welcome to the Egg Counter! " )
   print( "  If you have less than a billion eggs," )
   print( "  we'll help you count them, like the pros do." )
   print( "  You must enter the number of eggs as an integer." )
   
def main():
   try:
      eggs = int( input( "How many eggs? " ) )
   except:
      instructions()
      print( "   Please try again!" )
      return
   if( eggs < 0 ):
      print( "\n  Sorry, there's no way a chicken can un-lay eggs." )
      instructions()
      return
   elif( eggs > MAX_COUNT ):
      print( "\n  Oh, man ~ I can't count that high!!" )
      instructions()
      return
   else:
      greatGross = int(eggs / GREAT_GROSS)
      excessOverGG = eggs % GREAT_GROSS
      gross = int(excessOverGG / ONE_GROSS)
      excessOverGross = excessOverGG % ONE_GROSS
      dozens = int(excessOverGross / ONE_DOZEN)
      leftOver = int(excessOverGross % ONE_DOZEN)
      print( "  you have ", end=" " )
      if( greatGross > 0 ):
         print( "{} great gross ".format( greatGross ), end=" " )
      if( gross > 0 ):
         print( "{} gross ".format( gross ), end=" " )
      if( dozens > 0 ):
         print( "{} dozen ".format( dozens ), end=" " )
      if( leftOver > 0 ):
         print( "and {} eggs.".format( leftOver ) )


main()
          
