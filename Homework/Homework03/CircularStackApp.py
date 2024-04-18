###
# filename: CircularStackApp.py
# purpose:
# author:   Dr. Johnson
# date:     2023-
###

from CircularStack import CircularStack

def main():
   stack = CircularStack()
   print( "   pushing 23, 29, and 31 in that order..." )
   stack.push( 23 )
   stack.push( 29 )
   stack.push( 31 )
   stack.display()
   print( "   popping the top of the stack..." )
   stack.pop()
   stack.display()
   print( "   peeking at the top of the stack..." )
   print( "      top is: ", stack.peek() )
   print( "   popping the rest of the stack....." )
   stack.pop()
   stack.pop()
   stack.display()
   print( "   trying one extra 'pop()' operation..." )
   stack.pop()
   print( "   cased closed! " )

main()
