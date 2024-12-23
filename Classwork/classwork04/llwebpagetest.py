import llwebpage

myList = llwebpage.LinkedList()
print( "   List now has size: ", myList.getSize() )
myList.prepend( 23 )
myList.prepend( 19 )
myList.prepend( 17 )
myList.prepend( 13 )
myList.prepend( 11 )
myList.prepend(  7 )
myList.prepend(  5 )
myList.prepend(  3 )
myList.prepend(  2 )
print( "   List now has size: ", myList.getSize() )
myList.printList()                                    # just checking...
it = myList.getIteratorAt( 27 )                       # prints error msg.
it = myList.getIteratorAt( 0 )
print( "  Current node is: ", it.getCurrentData() )
it.next()
print( "  Current node is: ", it.getCurrentData() )
print( "  Current node has next? ", it.hasNext() )
it = myList.getIteratorAt( 0 )
while( it.hasNext() ):
   print( "  Current node value: ", it.getCurrentData() )
   it.next()
myList.insertAt( 4, 9 )
print( "   List now has size: ", myList.getSize() )
myList.printList()
myList.remove( 11 )
print( "   List now has size: ", myList.getSize() )
myList.printList()