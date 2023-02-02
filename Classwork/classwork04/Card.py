### 
# filename: Card.py 
# purpose:  simulation of a deck of playing cards
# author:   Dr. Johnson 
# date:     2023-01-07
### 

class Card:

   cardSuit = None
   cardRank = None

   def __init__( self, suit, rank ):
#      thisSet = { "♠", "♥", "♦", "♣" }      # can also do it with ASCII art
      thisSet = { "S", "H", "D", "C" }       # spades, hearts, diamonds, clubs
      myRank = [0, 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
      if( thisSet.isdisjoint( set( suit ) ) ):
         print( "   Illegal suit value sent to initializer." )
      elif( 1 > rank or 13 < rank ):
         print( "   Illegal card rank sent to initilaizer>" )
      else:
         self.cardSuit = suit
         self.cardRank = myRank[rank]

   def toString( self ):
      rep = "[{},{}]".format(str(self.cardSuit), str(self.cardRank))
      return rep

# this is for testing, and will be removed later....
spades = []
for i in range( 0, 13 ):
   c = Card( "S", i+1 )
   spades.append( c )
   print( "card: ", c.toString() )

