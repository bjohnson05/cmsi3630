###
# ffilename: sourceFille_todo.py
# purpose:   provides a file input reader
# author:    Dr. Johnsoson
# date:      20223-01-04
###

def readFile_todo( filename ):
   contents = "ACK not from file"
   try:
      ## TODO: fill in the lines to ~
      ##    open the file using the 'filename' argument
      ##    read the contents of the file into a buffer
      ##       the buffer should be named 'contents'
      ##    write out the buffer to the screen [optional]
      ##    close the file
      return contents
   except FileNotFoundError:
      print( "\n   Sorry, no such file found:", filename, ":" )
      return "err"
   except:
      print( "\n   Sorry, problem opening file ", filename )
      print( "   Make sure the file exists." )
      return "err"

def test():
   fileContent = readFile_todo( "test.txt")
   print( "\n   FILE 'test.txt' CONTENTS:\n" )
   print( fileContent )

## make sure to comment this line out when your are ready
##   to run for real
test()

