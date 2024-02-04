
import sys

MIN_SIZE = 2
MAX_SIZE = 40


ARGUMENT_COUNT_ERROR = "Exactly one command line argument required"
ARGUMENT_FORMAT_ERROR = "Argument must be an integer"
SIZE_ERROR = str.format( "Size must be between {} and {}", MIN_SIZE, MAX_SIZE )

def printTable( size ):
   width = 4 if (size < 32) else 5
   for i in range( 1, (size + 1) ):
      for j in range( 1, (size + 1) ):
         cell = "{0:{1}}".format( i * j, width )
         print( cell, end = "" )
      print()
   return

def main():

   size = 0
   try:
      count = len( sys.argv )
      size = int( sys.argv[1] )
      if( count == 1 ):
         print( ARGUMENT_COUNT_ERROR )
         return
      elif( (size < MIN_SIZE) or (size > MAX_SIZE) ):
         print( SIZE_ERROR )
         return
   except:
      print( ARGUMENT_FORMAT_ERROR )

   printTable( size );

main()
