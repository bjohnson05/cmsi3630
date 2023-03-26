###
# filename: QueueApp.py
# purpose:  homework03 problem 1
# author:   Dr. Johnson
# date:     2023-02-21
###

from Queue import Queue

class QueueApp:

   def __init__(self):
      myQueue = None

def main():
   print( "\n   Welcome to the Queue Test App\n" )
   size = int( input( "   Enter the size of your queue: " ) )

   myQueue = Queue( size )
   myQueue.remove()
   print( "   adding five items..." )
   myQueue.insert(  2 )
   myQueue.insert(  3 )
   myQueue.insert(  5 )
   myQueue.insert(  7 )
   myQueue.insert( 11 )
   print( "   trying to add a sixth item..." )
   myQueue.insert( 17 )
   myQueue.display()
   myQueue.display2()
   myQueue.remove()
   myQueue.remove()
   myQueue.remove()
   print( "   three items removed ~ queue of size ", myQueue.get_size(), " contains:" )
   myQueue.display()
   myQueue.display2()
   print( "   inserting two more items..." )
   myQueue.insert( 19 )
   myQueue.insert( 23 )
   myQueue.display()
   myQueue.display2()
   print( "   inserting two more items..." )
   myQueue.insert( 29 )
   myQueue.insert( 31 )
   myQueue.display()
   myQueue.display2()
   print( "   toggling remove and insert three times..." )
   myQueue.remove()
   myQueue.insert( 37 )
   myQueue.remove()
   myQueue.insert( 41 )
   myQueue.remove()
   myQueue.insert( 43 )
   myQueue.display()
   myQueue.display2()
   print( "   toggling remove and insert three more times..." )
   myQueue.remove()
   myQueue.insert( 47 )
   myQueue.remove()
   myQueue.insert( 53 )
   myQueue.remove()
   myQueue.insert( 57 )
   myQueue.display()
   myQueue.display2()

main()
