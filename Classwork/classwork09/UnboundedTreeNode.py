###
# filename: UnboundedTreeNode.py
# purpose:  unbounded tree demo
# author:   Dr. Johnson
# date:     2023-02-24
###

class UnboundedTreeNode:

   # the constructor
   def __init__( self, value ):
      self.data = value
      self.children = []
      self.num_kids = 0

   # add a child to the node
   #  children are in a list since this
   #  is an 'unbounded' tree node
   def add_child( self, child_value ):
      new_node = UnboundedTreeNode( child_value )
      self.children.append( new_node )
      self.num_kids += 1

   # fetch one child from this node's children
   def get_child( self, child_index ):
      if( child_index < 0 ):
         raise( "   Illegal Argument Exception..." )
      elif( child_index > self.num_kids ):
         raise( "   Illegal Argument Exception..." )
      else:
         return self.children[child_index]

   # return the value of this node's data
   def get_value( self ):
      return str( self.data )
