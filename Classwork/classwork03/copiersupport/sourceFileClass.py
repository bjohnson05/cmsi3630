###
# ffilename: sourceFille.py
# purpose:   provides a file input reader
# author:    Dr. Johnsoson
# date:      20223-01-04
###

class sourceFileClass():

   def __init__( self ):
      pass

   def readFile( self, filename ):
      try:
         fp = open( filename, "r" )
         contents = fp.read()      # reads the entire file
         return contents
      except FileNotFoundError:
         print( "\n   Sorry, no such file found:", filename, ":" )
         return "err"
      except:
         print( "\n   Sorry, problem opening file ", filename )
         print( "   Make sure the file exists." )
         return "err"

def test():
   sfc = sourceFileClass()
   fileContent = sfc.readFile( "test.txt")
   print( "\n   FILE 'test.txt' CONTENTS:\n" )
   print( fileContent )

test()
