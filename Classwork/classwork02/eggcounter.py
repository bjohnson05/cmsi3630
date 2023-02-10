"""
 An application that prompts the user for a number of eggs, and reports this
 number in grosses and dozens.
"""

import math

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
   elif( eggs >= 1000000000 ):
      print( "\n  Oh, man ~ I can't count that high!!" )
      instructions()
      return
   else:
      gross = eggs / 144
      excessOverGross = eggs % 144
      dozens = excessOverGross / 12
      leftOver = excessOverGross % 12
      print( "You have {} gross, {} dozen, and {} eggs.\n".format( gross, dozens, leftOver ) )

main()
          
