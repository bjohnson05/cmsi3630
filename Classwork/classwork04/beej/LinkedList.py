###
# filename: LinkedList.py
# purpose:  demonstrate a linked list in python
# author:   Dr. Johnson
# date:     2023-01-06
###

from ListNode import ListNode
from Iterator import Iterator

###
# this is the linked list itself
###
class LinkedList:
   head = None
   size = 0
   listCurrent = None
   it = None


  # constructor for the LinkedList
   def __init__( self ):
      self.head = None
      self.size = 0
      it = Iterator( self )

  # return the number of nodes in the list
   def getSize( self ):
      return self.size

  # add a ListNode to the FRONT of the list
   def prepend( self, dataToAdd ):
      currentHead = self.head
      self.head = ListNode( dataToAdd )
      self.head.nextNode = currentHead
      self.size += 1

  # helper method to print the list using a for loop
   def printList1( self ):
      currentNode = self.head
      for i in range( 0, self.getSize() ):
         print( currentNode.getData() )
         currentNode = currentNode.nextNode

  # get an Iterator that is pointing to a specific
  #   ListNode in the linked list
   def getIteratorAt( self, index ):
      if( index > self.size ):
         print( "   Sorry, getIteratorAt() ~ index out of range.\n" )
      else:
         it = Iterator( self )
         while( index > 0 ):
            it.currentNode = it.currentNode.nextNode
            index -= 1
         return it

  # helper method to print the list using the iterator's
  # methods and a while loop
   def printList2( self ):
      it = self.getIteratorAt( 0 )
      while( it.hasNext() ):
         print( it.getCurrentData(), end=", " )
         it.next()
      print( it.getCurrentData() )
