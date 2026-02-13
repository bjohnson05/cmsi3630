'''
filename: queue.py
purpose: demonstrate a queue using python's list
author: Dr. Johnson
Date: 2026-02-02
'''

class Queue:
   queue = []
   size = 0
   front = 0

   def __init__( self ):
      queue = list()
      size  = 0
      front = 0

   def insert( self, item ):
      self.queue.append( item )
      self.size += 1
      return self.size

   def remove( self ):
      returnValue = self.queue[self.front]
      self.front += 1
      return returnValue

   def peek( self ):
      return self.queue[self.front]

   def getSize( self ):
      return self.size

   def printqueue( self ):
      print( "   For reference, queue contains: ", self.queue )
      return True

def main():
   print( "\n\n   Python queue Tester" )
   print( "   ===================" )
   print( "\n   Making new queue:" );
   queue = Queue()
   queue.printqueue()
   queue.insert( 23 )
   queue.insert( 19 )
   queue.insert( 29 )
   queue.insert( 31 )
   queue.insert( 41 )
   queue.insert( 47 )
   print( "\n   Inserted six values to queue: " )
   print( "\n   Last item in queue is: ", queue.peek() )
   queue.printqueue()
   queue.insert(  2 )
   queue.insert(  3 )
   queue.insert(  5 )
   queue.insert(  7 )
   queue.insert( 11 )
   queue.insert( 13 )
   print( "\n   Inserted six more values to queue: " )
   print( "\n   Last item in queue is: ", queue.peek() )
   queue.printqueue()
   print( "\n   Removing value at FIFO end of queue: " )
   returnedValue = queue.remove()
   print( "\n   Returned value: ", returnedValue )
   print( "\n   Last item in queue is: ", queue.peek() )
   queue.printqueue()
   print( "\n   Removing value at FIFO end of queue: " )
   returnedValue = queue.remove()
   print( "\n   Returned value: ", returnedValue )
   print( "\n   Last item in queue is: ", queue.peek() )
   queue.printqueue()
   print( "\n   Peek at value at top of queue: " )
   returnedValue = queue.peek()
   print( "\n   Returned value: ", returnedValue )
   queue.printqueue()

main()
