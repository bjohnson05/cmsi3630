###
# filename: CircularIntLinkedList.py
# purpose:  homework03 linked list exercise
# author:   Dr. Johnson
# date:     2023-03-13
###

DEBUG = True

from Node import Node

class CircularIntLinkedList:

   current = None
   head = None
   size = 0

   def debug( self, message ):
      if( DEBUG ):
         print( message )
      return

   def __init__( self ):
      self.current = None
      self.size = 0

   def is_empty( self ):
      return self.size == 0

   def step( self ):
      self.current = self.current.next

   def insert( self, value ):
      if( self.is_empty() ):
         self.current = Node( value )
         self.current.next = self.current
         self.size += 1
      else:
         new_node = Node( value )
         new_node.next = self.current.next
         self.current.next = new_node
         self.size += 1
         self.current = self.current.next

   def display( self ):
      if( self.is_empty() ):
         print( "   List is empty." )
      else:
         for i in range( self.size ):
            print( "   Current Node Value: ", self.current.get_value() )
            self.current = self.current.next

   def search( self, value ):
      found = False
      for i in range( self.size ):
         if( self.current.get_value() == value ):
            found = True
            break
         else:
            self.current = self.current.next
      return found

   def remove( self, value ):
      if( self.is_empty() ):
         print( "   List is empty." )
         return
      else:
         if( self.search( value ) ):
            previous = self.current.next
            for i in range( self.size - 1 ):
               self.current = self.current.next
            self.current.next = self.current.next.next
            self.size -= 1
         return value

