###
# filename: LinkedList.py
# purpose:  demonstrate a linked list in python
# author:   Dr. Johnson
# date:     2023-01-06
###

from ListNode import ListNode

###
# this is the linked list itself
###
class LinkedList:
   head = None
   size = 0
   listCurrent = None

  # constructor for the LinkedList
   def __init__( self ):
      self.head = None
      self.size = 0

#   def __iter__( self ):
#      self.listCurrent = self.head
#      return self

#   def __next__( self ):
#      return self.listCurrent.nextNode

  # return the number of nodes in the list
   def getSize( self ):
      return self.size

  # add a ListNode to the FRONT of the list
   def prepend( self, dataToAdd ):
      currentHead = self.head
      self.head = ListNode( dataToAdd )
      self.head.nextNode = currentHead
      self.size += 1

  # helper method to print the list
   def printList1( self ):
      currentNode = self.head
      for i in range( 0, self.getSize() ):
         print( self.head.getData() )
         self.head = self.head.nextNode

  # get an Iterator that is pointing to a specific
  #   ListNode in the linked list
   # def getIteratorAt( self, index ):
   #    if( index > self.size ):
   #       print( "   Sorry, getIteratorAt() ~ index out of range.\n" )
   #    else:
   #       print( "   ...in getIteratorAt(), list.size is: ", self.getSize() )
   #       it = Iterator( self )
   #       it.current = self.head
   #       print( "   ...in getIteratorAt(), it.current is: ", it.current )
   #       print( "   ...in getIteratorAt(), list.head.data is:", it.getCurrentData() )
   #       while( index > 0 ):
   #          it.current = it.current.next
   #          index -= 1
   #       return it

