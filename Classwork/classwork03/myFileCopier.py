###
# filename: myFileCopier.py
# purpose:  demonstrate file handling in python
#           demonstrate multiple modules in python
#           demonstrate 'division of labor' in python
#              and in object-oriented programming
# author:   Dr. Johnson
# date:     2023-01-04
###

import copiersupport.sourceFile
import copiersupport.targetFile

def main():
   print( "\n\n   Welcome to the file duplicator!" )
   filename = input( "   Please enter the name of the file:" )
   fileContent = copiersupport.sourceFile.readFile( filename )
   copiersupport.targetFile.writeFile( filename, fileContent )


main()
