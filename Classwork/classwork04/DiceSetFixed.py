###
# filename: DiceSet.py
# purpose:  Dice game class example
# author:   Dr. Johnson
# date:     2023-01-06
###

import Die

class DiceSet:
   myDice = []
   counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  # constructor
   def __init__( self ):
      d1 = Die.Die( 6 )
      d2 = Die.Die( 6 )
      self.myDice.append( d1 )
      self.myDice.append( d2 )

  # track the count
   def count( self ):
      index = self.myDice[0].get_value() + self.myDice[1].get_value()
      self.counts[index] += 1
      return

  # roll all the dice one at a time
   def rollAll( self ):
      for i in range( 0, len(self.myDice) ):
         self.myDice[i].roll()
      return


def main():
  # a constant to define how many rolls
   MAX_ROLLS = 100000

  # instantiate the dice set
   dSet = DiceSet()

  # roll the dice
   for x in range( 1, MAX_ROLLS + 1 ):
      dSet.rollAll()
      dSet.count()

  # print the results
   print()
   for x in range( 2, len(dSet.counts) ):
      print( "{:2d} : {:8d}".format( x, dSet.counts[x] ) )

main()
