###
# filename: HeapNode.py
# purpose: binary heap demonstration
# author: Dr. Johnson
# date: 2023-03-04
###


class HeapNode:

   data = 0

   # constructor
   def __init__( self, value ):
      self.data = value

   # get the data value
   def get_data( self ):
      return int( self.data )

   # set the data value
   def set_data( self, value ):
      self.data = value

# hn = HeapNode( 23 )
# print( "   testing get_data()" )
# print( "   heap node: ", hn.get_data() )
# print( "   testing Set_data()" )
# hn.set_data( 42 )
# print( "   heap node: ", hn.get_data() )

