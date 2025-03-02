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
print( "   ...in LinkedListTest, list now has size: ", myList.getSize() )
print( "   ...in LinkedListTest, printing with LinkedList.printList1()..." )
myList.printList1()

print( "\n\n   ...IN LINKEDLISTTEST, TESTING getIteratorAt()..." )
it = myList.getIteratorAt( 0 )
print( "   ...in LinkedListTest, current node data is: ", it.getCurrentData() )
it.next()
print( "   ...in LinkedListTest, next current node data is: ", it.getCurrentData() )
it = myList.getIteratorAt( 3 )
print( "   ...in LinkedListTest, next current node data is: ", it.getCurrentData() )

print( "\n\n   ...IN LINKEDLISTTEST, TESTING printList2()..." )
myList.printList2()
