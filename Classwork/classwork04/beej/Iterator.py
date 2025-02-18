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
      print( "   ...in Iterator constructor, localList.size is: ", localList.getSize() )
      print( "   ...in Iterator constructor, printing localList..." )
      #localList.printList()
      currentNode = localList.head
      print( "   ...in Iterator constructor, currentNode is: ", currentNode )
      print( "   ...in Iterator constructor, localList.head is: ", localList.head )

  # set the next field of the current ListNode
  #   this will move the current 'pointer' down the line
   def next( self ):
      if( self.currentNode == None ):
         print( "   Looks like the list is empty." )
         return
      else:
         currentNode = currentNode.next

  # check if the current ListNode is the tail
   def hasNext( self ):
      return ( (currentNode != None) and (currentNode.next != None) )

  # helper method to get the current data value
   def getCurrentData( self ):
      return self.currentNode


