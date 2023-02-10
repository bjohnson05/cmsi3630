
import sys

MIN_SIZE = 1
MAX_SIZE = 20

ARGUMENT_COUNT_ERROR = "Exactly one command line argument required"
ARGUMENT_FORMAT_ERROR = "Argument must be an integer"
SIZE_ERROR = str.format( "Size must be between {} and {}", MIN_SIZE, MAX_SIZE )

def printTable( size ):
   for i in range( 1, (size + 1) ):
      for j in range( 1, (size + 1) ):
         cell = "{:4d}".format( i * j )
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
