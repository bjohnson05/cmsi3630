###
# filename: LinkedListTest.py
# purpose:  test the LinkedList demonstrator
# author:   Dr. Johnson
# date:     2023-01-08
###

import LinkedList

print( "\n\n   TESTING LINKEDLIST CLASS...\n" )
myList = LinkedList.LinkedList()

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
myList.printList1()

# it = iter( myList )
# it = myList.getIteratorAt( 0 )
# print( "  Current node is: ", next( it ) )
# it.next()
# print( "  Current node is: ", it.getCurrentData() )
