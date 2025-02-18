###
# this is the Node class for the list
###
class ListNode:
   data = 0       # the data field
   next = None    # the pointer to next ListNode

  # constructor for the ListNode
   def __init__( self, input = None ): # default value!
      self.data = input
      self.next = None

###
# the iterator class to MANAGE the list
###
class Iterator:
   current = None          # this is how the Iterator works

  # constructor for the Iterator
   def __init__( self, ll ):
      self.current = ll.head

  # set the next field of the current ListNode
  #   this will move the current 'pointer' down the line
   def next( self ):
      if( self.current == None ):
         return
      else:
         self.current = self.current.next

  # check if the current ListNode is the tail
   def hasNext( self ):
      return ( (self.current != None) and (self.current.next != None) )

  # helper method to get the current data value
   def getCurrentData( self ):
      return self.current.data

###
# this is the linked list itself
###
class LinkedList:
   head = None
   size = 0

  # constructor for the LinkedList
   def __init__( self ):
      head = ListNode()
      size = 0

  # return the number of nodes in the list
   def getSize( self ):
      return self.size

  # add a ListNode to the FRONT of the list
   def prepend( self, dataToAdd ):
      currentHead = self.head
      self.head = ListNode( dataToAdd )
      self.head.next = currentHead
      self.size += 1

  # get an Iterator that is pointing to a specific
  #   ListNode in the linked list
   def getIteratorAt( self, index ):
      if( index > self.size ):
         print( "   Sorry, getIteratorAt ~ index out of range.\n" )
         return None
      else:
         it = Iterator( self )
         while( index > 0 ):
            it.current = it.current.next
            index -= 1
         return it

  # a little helper method to print the list
  #   I just added this as a bonus
   def printList( self ):
      currentNode = self.head
      print( "\n", end="   " )
      for i in range( 0, self.size ):
         print( currentNode.data, end=" " )
         currentNode = currentNode.next
      print( "\n" )

  # the 'insertAt() method taking an index and a value
   def insertAt( self, index, value ):
      it = self.getIteratorAt( index - 1 )
      newNode = ListNode( value )
      newNode.next = it.current.next
      it.current.next = newNode
      self.size += 1

  # the 'remove()' method takes only a value to remove
   def remove( self, value ):
      it = self.getIteratorAt( 0 )
      while( it.hasNext() ):
         if( it.current.next.data != value ):
            it.next()
         else:
            retNode = it.current.next
            it.current.next = it.current.next.next
            self.size -= 1
            break
      return retNode
