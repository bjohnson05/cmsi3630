###
# filename: myFileCopier.todo.py
# purpose:  demonstrate file handling in python
#           demonstrate multiple modules in python
#           demonstrate 'division of labor' in python
#              and in object-oriented programming
# author:   Dr. Johnson
# date:     2023-01-04
###

from copiersupport.sourceFile import copiersupportReader
from copiersupport.targetFile import copiersupportWriter

file_reader = copiersupportReader()
file_writer = copiersupportWriter()

def main():
   try:
      print( "\n\nWelcome to the file duplicator!" )
      filename = input( "Please enter the name of the file being imported: \n" )
      copyFile = input( "Please enter the name of the file to be outputted: \n" )

      fileContentAndStatus = file_reader.readFile( filename )
      if fileContentAndStatus[1] == False:
         print("There was an error reading the source file!")
         exit()
      else:
         print("Successfully imported source file!")
      status = file_writer.writeFile( copyFile, fileContentAndStatus )
      if status == False:
         print("There was an error writing the output file!")
         exit()
      else:
         print("Successfully wrote to output file!")

   except Exception as exception:
      print( "Failed to start!\n" + str(exception) )

main()
