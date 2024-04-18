###
# filename: Deque.py
# purpose:  demonstration of a deque for homework03
# author:   Dr. Johnson
# date:     2023-03-13
###

DEBUG = False

class Deque:

   def __init__( self, size ):
      self.max_size = size
      self.count = 0
      self.l_front = 0
      self.l_rear = 0
      self.r_front = self.max_size - 1
      self.r_rear = self.max_size - 1
      self.the_deque = []
      for i in range( size ):
         self.the_deque.append( 0 )

   def debug( self, message ):
      if( DEBUG ):
         print( message )
      return

   def is_empty( self ):
      return self.count == 0

   def is_full( self ):
      return self.count == self.max_size

   def get_size( self ):
      return self.count

   def insert_left( self, value ):
      if( self.is_full() ):
         print( "   No room to insert, Deque is full." )
         return
      else:
         self.the_deque[self.l_rear] = value
         self.l_rear += 1
         self.count += 1
         return

   def insert_right( self, value ):
      if( self.is_full() ):
         print( "   No room to insert, Deque is full." )
         return
      else:
         self.the_deque[self.r_rear] = value
         self.r_rear -= 1
         self.count += 1
         return

   def remove_left( self ):
      if( self.is_empty() ):
         print( "   Nothing to remove, Deque is empty." )
         return
      else:
         self.l_rear -= 1
         value = self.the_deque[self.l_rear]
         self.the_deque[self.l_rear] = 0
         self.count -= 1
         return value

   def remove_right( self ):
      if( self.is_empty() ):
         print( "   Nothing to remove, Deque is empty." )
         return
      else:
         self.r_rear += 1
         value = self.the_deque[self.r_rear]
         self.the_deque[self.r_rear] = 0
         self.count -= 1
         return value

   def status( self ):
      self.debug( "   self.max_size is {0:3d}".format( self.max_size ) )
      for i in range( self.max_size ):
         self.debug( "      the_deque[{0:2d}] is: {1:3d}".format( i, self.the_deque[i] ) )
      return

   def display( self ):
      if( self.is_empty() ):
         print( "   Deque is empty, nothing to display." )
         return
      else:
         for i in range( self.l_rear ):
            if( self.the_deque[i] != 0 ):
               print( "[", self.the_deque[i], "]", end='' )
         for i in range( self.r_front, self.r_rear, -1 ):
            if( self.the_deque[i] != 0 ):
               print( "[", self.the_deque[i], "]", end='' )
         return print()


