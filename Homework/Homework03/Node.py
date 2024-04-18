###
# filename: Node.py
# purpose:  Node class for Linked List
# author:   Dr. Johnson
# date:     2023-02-21
###

class Node:
   def __init__( self, data ):
      self.data = data
      self.next = None

   def get_value( self ):
      return self.data

