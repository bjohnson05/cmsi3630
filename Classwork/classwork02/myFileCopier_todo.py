###
# filename: myFileCopier.todo.py
# purpose:  demonstrate file handling in python
#           demonstrate multiple modules in python
#           demonstrate 'division of labor' in python
#              and in object-oriented programming
# author:   Dr. Johnson
# date:     2023-01-04
###

import copiersupport.sourceFile_todo
import copiersupport.targetFile_todo

def main():
   print( "\n\n   Welcome to the file duplicator!" )
   filename = input( "   Please enter the name of the file:" )
   fileContent = copiersupport.sourceFile_todo.readFile_todo( filename )
   copiersupport.targetFile_todo.writeFile_todo( filename, fileContent )


main()
