"""
filename: LinkedListTest.py
purpose:  test the LinkedList demonstrator
author:   Dr. Johnson
date:     2023-01-08
"""

import LinkedList

my_list = LinkedList.LinkedList()

my_list.prepend( 23 )
my_list.prepend( 19 )
my_list.prepend( 17 )
my_list.prepend( 13 )
my_list.prepend( 11 )
my_list.prepend(  7 )
my_list.prepend(  5 )
my_list.prepend(  3 )
my_list.prepend(  2 )
print( "\n   List now has size:{}".format( my_list.getSize() ) )
my_list.print_list()
my_list.printme()

it = iter( my_list )
print()
for i in range( my_list.getSize() ):
   print( "   Current node is:{}".format( next(it).data ) )

print()
it = my_list.getIteratorAt( 3 )
print( "   got iterator at: ", it.list_current.data )
