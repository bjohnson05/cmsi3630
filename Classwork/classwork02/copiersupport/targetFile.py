###
# ffilename: targetFile.py
# purpose:   provides a file input reader
# author:    Dr. Johnsoson
# date:      20223-01-04
###

def writeFile( filename, buffer ):
   try:
      copyFile = filename + ".copy"
      tfp = open( copyFile, "w" )
      tfp.write( buffer )      # writes the entire file
      return
   except:
      print( "\n   Sorry, problem opening file:", copyFile, ":" )
      print( "   Make sure the file exists." )
      return "err"

def test():
   print( "  writing output file: ")
   writeFile( "test.txt", buffer )

# test()
