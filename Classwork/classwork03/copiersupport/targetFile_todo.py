###
# ffilename: targetFile_todo.py
# purpose:   provides a file input reader
# author:    Dr. Johnsoson
# date:      20223-01-04
###

def writeFile_todo( filename, buffer ):
   try:
      ## TODO: fill in the lines to ~
      ##    make the file name
      ##    open the file with the new name
      ##    write out the buffer to the file
      ##    close the file
      return
   except:
      print( "\n   Sorry, problem opening file:", copyFile, ":" )
      print( "   Make sure the file exists." )
      return "err"

def test():
   print( "  writing output file: ")
   buffer = "this is a test string for the buffer\n"
   print( "    buffer: ", buffer )
   writeFile_todo( "test.txt", buffer )

## make sure to comment this line out when your are ready
##   to run for real
test()
