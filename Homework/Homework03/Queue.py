###
# filename: Queue.py
# purpose:  homework03 problem 1
# author:   Dr. Johnson
# date:     2023-02-21
###

class Queue:


   def __init__(self, max_size):
      self.QUEUE_MAX_SIZE = max_size
      self.a = []
      self.front = 0
      self.count = 0
      self.rear  = 0
      for i in range( self.QUEUE_MAX_SIZE ):
         self.a.append( None )

   def insert( self, value ):
      if( self.count == self.QUEUE_MAX_SIZE ):
         print( "   Sorry, Queue is full, no room to insert ", value )
         return False
      else:
         self.a[self.rear] = value
         self.count = self.count + 1
         self.rear  = self.rear  + 1
         if( self.rear == self.QUEUE_MAX_SIZE ):
            self.rear = 0
         return True


   def remove( self ):
      if( self.count == 0 ):
         print( "   Sorry, Queue is empty, nothing to remove." )
         return False
      else:
         value = self.a[self.front]
         self.a[self.front] = None
         self.count = self.count - 1
         self.front = self.front + 1
         if( self.front == self.QUEUE_MAX_SIZE ):
            self.front = 0
         return value

   def get_size( self ):
      return self.count


   def display( self ):
      if( self.rear > self.front ):
         for i in range( self.front, self.rear ):
            print( "   element[", i, "] is: ", self.a[i] )
      else:
         for i in range( self.front, self.QUEUE_MAX_SIZE ):
            print( "   element[", i, "] is: ", self.a[i] )
         for i in range( 0, self.front ):
            print( "   element[", i, "] is: ", self.a[i] )
      return

   def display2( self ):
      print( "   ", end="" )
      if( self.rear > self.front ):
         for i in range( self.front, self.rear ):
            print( "[", self.a[i], "]", end=" "  )
      else:
         for i in range( self.front, self.QUEUE_MAX_SIZE ):
            print( "[", self.a[i], "]", end=" "  )
         for i in range( 0, self.front ):
            print( "[", self.a[i], "]", end=" "  )
      print()
      return

