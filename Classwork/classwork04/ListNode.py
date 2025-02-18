class ListNode:
   data = 0       # for data storage
   next = None    # reference to the next node
  # the constructor
   def __init__( self, input ):
      self.data = input
      self.next = None

#  test it out; to be removed later
ln = ListNode( 37 )
print( "   ln.data is: ", ln.data )
            