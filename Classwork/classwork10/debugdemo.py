###
# filename: debugdemo.py
# purpose:  demonstrate a way to put debug statements
#           in code that don't have to be removed or
#           commented out
# author:   Dr. Johnson
# date:     2023-03-11
###

DEBUG_ON = False

def debug( message ):
   if DEBUG_ON:
      print( "  ", message )

def main():
   debug( "This is a test debug message" )
   print( "   Hello, world!" )

main()
