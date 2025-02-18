###
# filename: ListNode.py
# purpose:  demonstrate a linked list in python
# author:   Dr. Johnson
# date:     2023-01-06
###

class ListNode:
   data = 0
   next = None

   def __init__( self, input ):
      self.data = input
      self.next = None

   def getData( self ):
      return self.data

# test it out
print( "\n\n   TESTING LISTNODE CLASS...\n" )
ln = ListNode( 37 )
print( "   ln.data is: ", ln.getData() )

