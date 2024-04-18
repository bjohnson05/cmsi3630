import sys

def convert( blah ):
   total = 0
   for x in blah[1:]:
      total += 1.0 / float( x )
   total = 1.0 / total
   return total


print( "total parallel resistance: ", convert( sys.argv ), " ohms." )

   