###
# filename: TruckLoader.py
# purpose: binary heap demonstration
# author: Dr. Johnson
# date: 2023-03-19
###

from BinaryHeap import BinaryHeap

def loader():
   sum = 0
   heap = BinaryHeap()
   print( "\n\n   WELCOME TO THE TRUCK LOADER PROGRAM\n" )
   print( "   Loads to be put on the trailer: " )
   heap.insert(2000)
   heap.insert(1000)
   heap.insert(500)
   heap.insert(3000)
   heap.insert(1234)
   heap.insert(2129)
   heap.insert(1800)
   heap.insert(700)
   heap.insert(1350)
   heap.insert(9800)
   heap.insert(1760)
   heap.insert(5280)
   heap.insert(876)
   heap.insert(4500)
   print( "   The heap contains: " )
   heap.print_heap()
   order = []
   for i in range( heap.get_size() ):
      order.append( heap.delete() )
   print( "   Load the truck in the following order:" )
   for i in order:
      print( "   {0:5d} lb. load".format(i.get_data()) )
      sum += i.get_data()
   print( "   Total weight: ", sum, " pounds." )

loader()
