import math
import random

def getRandomPoint():
   xmult = round( random.random() )
   ymult = round( random.random() )
   a = random.random()
   b = random.random()
   if( xmult ):
      a *= -1
   if( ymult ):
      b *= -1
   c = math.sqrt( (a * a) + (b * b) )
   return c

def dartThrow( inHits ):
   if( getRandomPoint() < 1.0 ):
      return inHits + 1
   else:
      return inHits

def main():
   hits = 0
   numberOfDarts = int( input( "\n   Enter the number of darts to throw: ") )
   if( numberOfDarts < 1000 ):
      print( "   You need more than 1000 darts.  Try again.\n\n" )
   else:
      i = 0
      while( i < numberOfDarts ):
         hits = dartThrow( hits )
         i += 1
      approxPI = 4.0 * (float( hits ) / float( numberOfDarts ) )
      print( "\n      Real value of PI: ", math.pi)
      print( "   Approximation of PI: ", approxPI )

main()

