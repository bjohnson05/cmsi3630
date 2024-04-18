###
# filename: BinaryTreeNode.py
# purpose: binary tree demonstrator
# author:   Dr. Johnson
# date:     2023-02-23
###

class BinaryTreeNode:

   # the constructor
   def __init__( self, value ):
      self.data  = value
      self.left  = None
      self.right = None

   # add a child to the node
   def add_child( self, value, child ):
      child = child.upper()
      if( child == "L"  ):
         self.left = BinaryTreeNode( value )
      elif( child == "R" ):
         self.right = BinaryTreeNode( value )
      else:
         raise( "   Illegal Argument Exception..." )

   # get one child from this parent node
   def get_child( self, child ):
      child = child.upper()
      if( child == "L" ):
         return self.left
      elif( child == "R" ):
         return self.right
      else:
         raise( "   Illegal Argument Exception..." )

   # get this node's data value
   def get_data( self ):
       return self.data

