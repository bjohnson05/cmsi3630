###
# filename: BinaryHeap.py
# purpose: binary heap demonstration
# author: Dr. Johnson
# date: 2023-03-04
###

from HeapNode import HeapNode

class BinaryHeap:

   uriah = []     # does anyone get this reference?  Nobody has read 'David Copperfield'??
   size  = 0

   def __init__( self ):
      self.uriah = []
      return

   # First some low-hanging fruit let's do the traversal helpers that do the
   #  indexing operations we'll need to use to find stuff in the heap
   def get_parent( self, index ):
      return self.uriah[(int)((index - 1) / 2)]

   def get_child( self, index, child ):
      result = (index * 2) + 1
      if( child.upper() == 'R'):       # make sure we're case insensitive!
         result += 1
      return self.uriah[result]

   # this just prints the array values; it's left to the observer to figure out
   #  which HeapNode is which, in terms of parent and child
   def print_heap( self ):
      for i in self.uriah:
         print( "[", i.get_data(), "]", end = "" )
      print( " ~ size is: ", self.size )

   # Now we can handle insertions.  ArrayList has a nice "add" method
   #  that makes things easy.  We *DO* have to deal with the primitive
   #  to Object situation, but that is trivial...
   def insert( self, value ):
      self.uriah.append( HeapNode( value ) )
      self.bubble_up( self.size )                # WOW that was easy!
      self.size += 1

   # Here is the bubble method that does the swappy thang....
   #  Whaddya mean?!  OF COURSE it is recursive!  Fuggeddaboutit...
   def bubble_up( self, index ):
      if( index == 0 ):     # base case:
         return             #  we are already at the root, so we are done

      parent = self.get_parent( index )
      parent_index = (int)((index -1) / 2)
      if( self.uriah[parent_index].get_data() < self.uriah[index].get_data() ):
         temp = self.uriah[index]
         self.uriah[index] = self.uriah[parent_index]
         self.uriah[parent_index] = temp
         self.bubble_up( parent_index )

   # Adding in the deletions code.  Python list istmakes it easy to find the
   #  last node because it's at the end of the list.  We just need to swap it
   #  with the root at element [0], then trickle it down.
   def delete( self ):
      return_node = self.uriah[0]                      # save the root node
      self.size = self.size - 1                       # decrement size before use
      self.uriah[0] = self.uriah[self.size]           # move the last node to root
      self.trickle_down( 0 )                           # re-heapify
      self.uriah.pop(self.size)
      return return_node

   # Here is the trickle down method that does the swappy thing in the
   #  other direction, from the root downward.
   def trickle_down( self, index ):
      next_index = (index * 2) + 1            # the child to compare
      if( next_index >= self.size ):          # base case
         return
      root = self.uriah[index]
      next = None
      if( int(self.get_child( index, 'L' ).get_data()) > int(self.get_child( index, 'R' ).get_data()) ):
         next = self.get_child( index, 'L' )
      else:
         next = self.get_child( index, 'R' )
         next_index += 1
      if( self.uriah[index].get_data() < self.uriah[next_index].get_data() ):
         self.uriah[index] = next
         self.uriah[next_index] = root
      self.trickle_down( next_index )

   # See if the heap is empty or not
   def isEmpty( self ):
     return self.uriah.isEmpty()

   # Get the size of the heap
   def get_size( self ):
      return self.size

