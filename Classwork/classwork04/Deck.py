### 
# filename: Deck.py 
# purpose:  simulation of a deck of playing cards
# author:   Dr. Johnson 
# date:     2023-01-11
### 

import Card
import random

class Deck:
   suits   = [ "S", "H", "D", "C" ]
   theDeck = []

   def __init__( self ):
      for s in self.suits:
         for i in range( 0, 13 ):
            c = Card.Card( s, i+1 )
            self.theDeck.append( c )

   def shuffle( self ):
      for i in range( len(self.theDeck) ):
         j = random.randint(0, 51)
         c1 = self.theDeck[i]
         c2 = self.theDeck[j]
         self.theDeck[i] = c2
         self.theDeck[j] = c1

   def cardAt( self, index ):
      try:
         return self.theDeck[index]
      except:
         print( "   Bad index in 'cardAt()' method.\n" )


   def deal( self, cardCount ):
      hand = []
      for i in range( cardCount ):
         hand.append( self.cardAt( i ).toString() )
         self.theDeck.pop(i)
      return hand


d = Deck()
for i in range( len(d.theDeck) ):
   print( d.theDeck[i].toString(), end = " " )
print()
d.shuffle()
print("\n\n    AFTER SHUFFLING:" )
for i in range( len(d.theDeck) ):
   print( d.theDeck[i].toString(), end = " " )
print()
myHand = []
myHand = d.deal( 5 )
print( "\n  my hand: ", myHand )
print("\n\n    AFTER DEALING ONE HAND:" )
for i in range( len(d.theDeck) ):
   print( d.theDeck[i].toString(), end = " " )
print()
