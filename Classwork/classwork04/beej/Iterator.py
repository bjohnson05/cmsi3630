###
# filename: Iterator.py
# purpose:  demonstrate a linked list in python
# author:   Dr. Johnson
# date:     2023-01-06
###

from ListNode import ListNode

class Iterator:
   currentNode = None

  # constructor for the Iterator
   def __init__( self, localList ):
      self.currentNode = localList.head
      if( self.currentNode == None ):
         print( "   ...in Iterator constructor, list is currently empty." )

  # set the next field of the current ListNode
  #   this will move the current 'pointer' down the line
   def next( self ):
      if( self.currentNode == None ):
         print( "   Looks like the list is empty." )
         return
      else:
         self.currentNode = self.currentNode.nextNode

  # check if the current ListNode is the tail
   def hasNext( self ):
      return ( (self.currentNode != None) and (self.currentNode.nextNode != None) )

  # helper method to get the current data value
   def getCurrentData( self ):
      return self.currentNode.getData()


