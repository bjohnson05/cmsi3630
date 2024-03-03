import random

class RBNode:
   def __init__( self, val ):
      self.red = False
      self.parent = None
      self.val = val
      self.left = None
      self.right = None

class RBTree:
   def __init__( self ):
      self.nil = RBNode( 0 )
      self.nil.red = False
      self.nil.left = None
      self.nil.right = None
      self.root = self.nil

   def insert( self, val ):
      # Ordinary Binary Search Insertion
      new_node = RBNode( val )
      new_node.parent = None
      new_node.left = self.nil
      new_node.right = self.nil
      new_node.red = True  # new node must be red

      parent = None

      current = self.root

      while current != self.nil:
         parent = current
         if new_node.val < current.val:
            current = current.left
         elif new_node.val > current.val:
            current = current.right
         else:
            return

      # Set the parent and insert the new node
      new_node.parent = parent
      if parent == None:
         self.root = new_node
      elif new_node.val < parent.val:
         parent.left = new_node
      else:
         parent.right = new_node

      # Fix the tree
      self.fix_insert( new_node )

   def fix_insert( self, new_node ):
      while new_node != self.root and new_node.parent.red:
         if new_node.parent == new_node.parent.parent.right:
            u = new_node.parent.parent.left  # uncle
            if u.red:
               u.red = False
               new_node.parent.red = False
               new_node.parent.parent.red = True
               new_node = new_node.parent.parent
            else:
               if new_node == new_node.parent.left:
                  new_node = new_node.parent
                  self.rotate_right( new_node )
               new_node.parent.red = False
               new_node.parent.parent.red = True
               self.rotate_left( new_node.parent.parent )
         else:
            u = new_node.parent.parent.right  # uncle
            if u.red:
               u.red = False
               new_node.parent.red = False
               new_node.parent.parent.red = True
               new_node = new_node.parent.parent
            else:
               if new_node == new_node.parent.right:
                  new_node = new_node.parent
                  self.rotate_left( new_node )
               new_node.parent.red = False
               new_node.parent.parent.red = True
               self.rotate_right( new_node.parent.parent )
      self.root.red = False

   def exists( self, val ):
      curr = self.root
      while curr != self.nil and val != curr.val:
         if val < curr.val:
            curr = curr.left
         else:
            curr = curr.right
      return curr

   # rotate left at node x
   def rotate_left( self, x ):
      y = x.right
      x.right = y.left
      if y.left != self.nil:
         y.left.parent = x

      y.parent = x.parent
      if x.parent == None:
         self.root = y
      elif x == x.parent.left:
         x.parent.left = y
      else:
         x.parent.right = y
      y.left = x
      x.parent = y

    # rotate right at node x
   def rotate_right( self, x ):
      y = x.left
      x.left = y.right
      if y.right != self.nil:
         y.right.parent = x

      y.parent = x.parent
      if x.parent == None:
         self.root = y
      elif x == x.parent.right:
         x.parent.right = y
      else:
         x.parent.left = y
      y.right = x
      x.parent = y

   def __repr__( self ):
      lines = []
      print_tree( self.root, lines )
      return '\n'.join( lines )

def print_tree( node, lines, level=0 ):
   if node.val != 0:
      print_tree( node.left, lines, level + 1 )
      lines.append( '-' * 4 * level + '> ' +
                  str( node.val ) + ( 'R' if node.red else 'B' ) )
      print_tree( node.right, lines, level + 1 )

def in_order_printer( current_node ):
   if( current_node == None ):
      return
   else:
      in_order_printer( current_node.get_child( "L" ) )
      print( "( ", current_node.get_data( ), " )", end="" )
      in_order_printer( current_node.get_child( "R" ) )

def get_nums( num ):
   random.seed( 1 )
   nums = []
   for _ in range( num ):
      nums.append( random.randint( 1, num-1 ) )
   return nums

def main( ):
   tree = RBTree( )
   tree.insert( 23 )
   tree.insert( 17 )
   tree.insert( 29 )
   tree.insert( 13 )
   tree.insert( 19 )
   tree.insert( 11 )
   tree.insert( 15 )
   tree.insert(  7 )
   tree.insert(  5 )
   tree.insert( 31 )
   tree.insert( 37 )
   tree.insert( 27 )
   print( tree )

main( )
