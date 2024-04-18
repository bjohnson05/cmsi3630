###
# filename: CircularStack.py
# purpose:  homework03 problem
# author:   Dr. Johnson
# date:     2023-03-16
###

from CircularIntLinkedList import LinkedList

class CircularStack( LinkedList ):

   def __init__( self ):
      self.my_list = LinkedList()

   def push( self, value ):
      self.my_list.insert( value )
      return

   def pop( self ):
      return self.my_list.remove( self.my_list.current.get_value() )

   def peek( self ):
      return self.my_list.current.get_value()

   def display( self ):
      self.my_list.display()

