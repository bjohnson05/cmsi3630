'''
filename: stack.py
purpose: demonstrate a stack using python's list
author: Dr. Johnson
Date: 2026-02-02
'''

class Stack:
   stack = []
   size = 0

   def __init__( self ):
      stack = list()
      size  = 0

   def push( self, item ):
      self.stack.append( item )
      self.size += 1
      return self.size

   def pop( self ):
      self.size -= 1
      return self.stack.pop(self.size)

   def peek( self ):
      return self.stack[self.size - 1]

   def getSize( self ):
      return self.size

   def printStack( self ):
      print( "   For reference, stack contains: ", self.stack )
      return True

def main():
   print( "\n\n   Python Stack Tester" )
   print( "   ===================" )
   print( "\n   Making new stack:" );
   stack = Stack()
   stack.printStack()
   stack.push( 23 )
   stack.push( 19 )
   stack.push( 29 )
   stack.push( 31 )
   stack.push( 41 )
   stack.push( 47 )
   print( "\n   Added six values to stack: " )
   print( "\n   Top of stack is: ", stack.peek() )
   stack.printStack()
   stack.push(  2 )
   stack.push(  3 )
   stack.push(  5 )
   stack.push(  7 )
   stack.push( 11 )
   stack.push( 13 )
   print( "\n   Added six more values to stack: " )
   print( "\n   Top of stack is: ", stack.peek() )
   stack.printStack()
   print( "\n   Removing value at top of stack: " )
   returnedValue = stack.pop()
   print( "\n   Returned value: ", returnedValue )
   print( "\n   Top of stack is: ", stack.peek() )
   stack.printStack()
   print( "\n   Removing value at top of stack: " )
   returnedValue = stack.pop()
   print( "\n   Returned value: ", returnedValue )
   print( "\n   Top of stack is: ", stack.peek() )
   stack.printStack()
   print( "\n   Peek at value at top of stack: " )
   returnedValue = stack.peek()
   print( "\n   Returned value: ", returnedValue )
   stack.printStack()

main()
